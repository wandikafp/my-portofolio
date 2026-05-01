import streamlit as st
from model.model_loader import load_model, load_eval_data

# Page Config
st.set_page_config(
    page_title="My Portfolio",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Global State & Caching
@st.cache_resource
def get_model():
    return load_model()

@st.cache_resource
def get_eval_data():
    return load_eval_data()

# Initialize model in session state
if "model" not in st.session_state:
    try:
        st.session_state.model = get_model()
        st.session_state.eval_data = get_eval_data()
        st.session_state.model_loaded = True
    except FileNotFoundError as e:
        st.session_state.model_loaded = False
        st.session_state.load_error = str(e)

# Sidebar Global
with st.sidebar:
    st.title("🧭 Navigasi")
    st.markdown("---")
    # Navigation is handled by Streamlit pages automatically
    st.markdown("### 📦 Status Model")
    if st.session_state.get("model_loaded"):
        st.success("✅ Model siap digunakan")
    else:
        st.error("❌ Model tidak ditemukan")
        st.caption(f"`{st.session_state.get('load_error', '')}`")
    
    st.markdown("---")
    st.caption("💡 Tip: Gunakan sidebar untuk navigasi antar halaman")

st.switch_page("pages/1_🏠_Home.py")