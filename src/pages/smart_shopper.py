import os
import streamlit as st
import json
from google.genai import types
from projects.smart_shopper.config import get_agent_client
from projects.smart_shopper.tools import get_product_info, get_material_safety

# ==========================================
# 1. SETUP UI & CSS
# ==========================================
st.set_page_config(page_title="Smart Shopper AI", page_icon="🛍️", layout="centered")

# Load Custom CSS from file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS_PATH = os.path.join(BASE_DIR, "projects", "smart_shopper", "style.css")

try:
    with open(CSS_PATH, "r") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("Custom CSS not found.")

# ==========================================
# 2. AGENT INITIALIZATION
# ==========================================
genai_client = get_agent_client()

system_instruction = """You are a smart shopping assistant named 'Smart Shopper'. \
Your task is to help the user find products and provide the best recommendations \
based on their criteria. Call the search tools to retrieve data from the database.\n\n\
IMPORTANT: Your final output MUST be in raw JSON format without any markdown formatting (```json). \
Use exactly this schema:\n\
{\n\
  "thought_process": "Your thought process regarding the user's request",\n\
  "recommendations": [\n\
    {\n\
      "asin": "Product ID",\n\
      "title": "Product Name",\n\
      "brand": "Product Brand",\n\
      "price": 12.99,\n\
      "reason": "Short reason why the product is recommended"\n\
    }\n\
  ],\n\
  "agent_message": "A friendly greeting message to the user"\n\
}"""

if "chat_session" not in st.session_state:
    st.session_state.chat_session = genai_client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            tools=[get_product_info, get_material_safety],
            system_instruction=system_instruction,
            temperature=0.3
        )
    )

# ==========================================
# 3. STREAMLIT UI LOGIC
# ==========================================
st.title("🛍️ Smart Shopper AI")
st.caption("Your personal AI shopping assistant powered by Gemini & MongoDB Vector Search.")

# Inisialisasi riwayat chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Fungsi untuk me-render product card
def render_product_card(rec):
    st.markdown(f"""
    <div class="product-card">
        <div class="product-title">{rec.get('title', 'Unknown Product')}</div>
        <div class="product-brand">{rec.get('brand', 'Unknown Brand')}</div>
        <div class="product-price">${rec.get('price', 0.0)}</div>
        <div class="product-reason">{rec.get('reason', '')}</div>
    </div>
    """, unsafe_allow_html=True)

# Tampilkan history chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg["role"] == "assistant" and "data" in msg:
            data = msg["data"]
            if data.get("recommendations"):
                for rec in data["recommendations"]:
                    render_product_card(rec)

# Input Chat
if prompt := st.chat_input("I am looking for a running shoe under $50..."):
    # 1. Tampilkan pesan user
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Proses pesan ke Agent
    with st.chat_message("assistant"):
        with st.spinner("Searching the catalog..."):
            try:
                response = st.session_state.chat_session.send_message(prompt)
                
                # Bersihkan JSON string
                text = response.text.strip()
                if text.startswith('```json'): text = text[7:]
                if text.endswith('```'): text = text[:-3]
                
                # Parse JSON
                try:
                    result_data = json.loads(text.strip())
                    agent_msg = result_data.get("agent_message", "I found something for you.")
                    
                    st.markdown(agent_msg)
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": agent_msg,
                        "data": result_data
                    })
                    
                    if result_data.get("thought_process"):
                        with st.expander("🤔 View AI Thought Process"):
                            st.write(result_data["thought_process"])
                            
                    if result_data.get("recommendations"):
                        for rec in result_data["recommendations"]:
                            render_product_card(rec)
                            
                except Exception as e:
                    st.error(f"Failed to parse agent response: {e}")
                    st.code(response.text)
                    
            except Exception as e:
                st.error(f"Agent encountered an error: {e}")
