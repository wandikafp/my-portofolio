import streamlit as st
import base64
from pathlib import Path

def get_image_base64(image_path: str) -> str:
    """Convert a local image to a base64 data URI string."""
    path = Path(image_path)
    if not path.exists():
        return ""
    suffix = path.suffix.lower().lstrip(".")
    mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg",
            "webp": "image/webp", "gif": "image/gif", "svg": "image/svg+xml"}
    mime_type = mime.get(suffix, "image/png")
    data = base64.b64encode(path.read_bytes()).decode()
    return f"data:{mime_type};base64,{data}"

def load_css():
    """Load and inject the global CSS stylesheet."""
    css_path = Path(__file__).parent.parent / "styles" / "main.css"
    if css_path.exists():
        st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)