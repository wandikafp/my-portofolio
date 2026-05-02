# INI HANYA SEBAGAI CONTOH
import streamlit as st
import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import PGVector
from langchain_core.prompts import PromptTemplate, MessagesPlaceholder
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_classic.chains import create_history_aware_retriever, create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory

load_dotenv()

st.set_page_config(
    page_title="SafeBank Assistant",
    page_icon="🏦",
    layout="centered"
)


@st.cache_resource
def load_chain():
    api_key = os.getenv("GROQ_API_KEY")
    CONNECTION_STRING = "postgresql+psycopg2://langchain:langchain@localhost:5432/langchain"
    # Nama collection di pgVector (bebas)
    COLLECTION_NAME = "bot_docs"

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.2,
        api_key=api_key,
        max_tokens=1024,
        timeout=None,
        max_retries=3,
    )

    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = PGVector(
        collection_name=COLLECTION_NAME,
        connection_string=CONNECTION_STRING,
        embedding_function=embedding, # Model embedding yang sama
    )
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})

    context_q_system_prompt = (
        "Given the following chat history and the follow-up question which might reference "
        "context in the chat history, rephrase the follow-up question to be a standalone question "
        "which can be understood without the chat history. "
        "Do NOT answer the question, just reformulate it if needed and otherwise return it as is."
    )

    context_q_prompt = ChatPromptTemplate.from_messages([
        ("system", context_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "Question: {input}"),
    ])

    history_aware_retriever = create_history_aware_retriever(
        llm=llm,
        retriever=retriever,
        prompt=context_q_prompt,
    )

    qa_system_prompt = (
        "You are a helpful customer service assistant for SafeBank. "
        "Answer the user's question based on the provided context."
    )

    qa_prompt = ChatPromptTemplate.from_messages([
        ("system", qa_system_prompt),
        MessagesPlaceholder("chat_history"),
        (
            "human",
            "Question: {input}\nContext: {context}\n"
            "Please provide a concise and accurate answer based on the context provided. "
            "If the context does not contain sufficient information to answer the question, "
            'respond with "I don\'t know."',
        ),
    ])

    qa_chain = create_stuff_documents_chain(llm, qa_prompt)
    rag_chain = create_retrieval_chain(history_aware_retriever, qa_chain)

    return rag_chain


if "store" not in st.session_state:
    st.session_state.store = {}

if "messages" not in st.session_state:
    st.session_state.messages = []

if "session_id" not in st.session_state:
    st.session_state.session_id = "session_1"


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in st.session_state.store:
        st.session_state.store[session_id] = ChatMessageHistory()
    return st.session_state.store[session_id]

with st.sidebar:
    st.title("🏦 SafeBank Assistant")
    st.markdown("Tanya apa saja tentang produk & layanan SafeBank.")
    st.divider()

    st.subheader("Session")
    session_id_input = st.text_input("Session ID", value=st.session_state.session_id)
    if session_id_input != st.session_state.session_id:
        st.session_state.session_id = session_id_input
        st.session_state.messages = []

    if st.button("🗑️ Hapus Riwayat Chat"):
        st.session_state.messages = []
        st.session_state.store.pop(st.session_state.session_id, None)
        st.rerun()

    st.divider()
    st.caption("Powered by Groq · LangChain · FAISS")


st.header("💬 SafeBank Chatbot")
st.caption("Asisten virtual untuk informasi produk dan layanan SafeBank")

# Render existing messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle new user input
if user_input := st.chat_input("Tulis pertanyaan kamu di sini..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Sedang mencari jawaban..."):
            rag_chain = load_chain()
            chain_with_history = RunnableWithMessageHistory(
                rag_chain,
                get_session_history,
                input_messages_key="input",
                history_messages_key="chat_history",
                output_messages_key="answer",
            )
            result = chain_with_history.invoke(
                {"input": user_input},
                config={"configurable": {"session_id": st.session_state.session_id}},
            )
            answer = result["answer"]
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
