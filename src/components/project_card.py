"""Project card component for grid display."""

import streamlit as st
from dto.Project import Project
from utils.helpers import get_image_base64


def render_project_card(project: Project, key_prefix: str = "card"):
    """
    Render project card yang dapat diklik untuk navigasi ke detail.
    
    Args:
        project: Objek Project yang akan ditampilkan
        key_prefix: Prefix untuk key komponen Streamlit (unik per halaman)
    """
    card_key = f"{key_prefix}_{project.id}"
    
    with st.expander(f"🔹 {project.title}", expanded=False):
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.markdown(f"**📝 Deskripsi:** {project.description}")
            st.markdown(f"**🛠️ Tools:** {', '.join(project.tools)}")
            
            # Tombol navigasi ke detail
            if st.button("🔍 Lihat Detail →", key=f"{card_key}_btn"):
                st.query_params["project"] = project.id
                st.rerun()
        
        img_src = get_image_base64(project.image_url)
        with col2:
            if img_src:
                st.image(
                    img_src, 
                    use_column_width=True,
                    caption=project.title
                )
            else:
                st.markdown(f'<div class="project-thumb" style="background:linear-gradient(135deg,'
            'rgba(108,99,255,0.15),rgba(59,130,246,0.1));display:flex;'
            'align-items:center;justify-content:center;font-size:3rem;">🛰️</div>', unsafe_allow_html=True)