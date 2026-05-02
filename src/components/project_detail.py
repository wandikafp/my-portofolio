import streamlit as st
from dto.Project import Project
from utils.helpers import get_image_base64

def render_project_detail(project: Project, show_back_button: bool = True):
    """
    Render halaman detail proyek dengan informasi lengkap.
    
    Args:
        project: Objek Project yang akan ditampilkan
        show_back_button: Apakah menampilkan tombol kembali ke list
    """
    is_internal_page = project.demo_url.startswith("__page__:")
    internal_page_path = project.demo_url.replace("__page__:", "") if is_internal_page else None
    # Tombol kembali
    if show_back_button:
        if st.button("← Kembali ke Daftar Proyek"):
            st.query_params.pop("project", None)
            st.rerun()
        st.markdown("---")
    
    # Header Proyek
    col_header, col_actions = st.columns([4, 1])
    
    with col_header:
        st.title(project.title)
        st.markdown(f"*{project.description}*")
    
    with col_actions:
        if project.github_url:
            st.link_button("🐙 GitHub", project.github_url)
        if is_internal_page and internal_page_path:
            if st.button("🌐 Live Demo"):
                st.switch_page(internal_page_path)
        elif project.demo_url:
            st.link_button("🌐 Live Demo", project.demo_url)
    
    # Hero Image
    img_src = get_image_base64(project.image_url)
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
    
    # Long Description
    st.subheader("📋 Tentang Proyek")
    st.markdown(project.long_description)
    
    # Metrics (jika ada)
    if project.metrics:
        st.subheader("📊 Metrik & Hasil")
        metric_cols = st.columns(len(project.metrics))
        for i, (label, value) in enumerate(project.metrics.items()):
            metric_cols[i].metric(label, value)
    
    # Tools Used
    st.subheader("🛠️ Technologies Used")
    tools_badges = " ".join([f"`{tool}`" for tool in project.tools])
    st.markdown(tools_badges)
    
    # Challenges & Solutions (jika ada)
    if project.challenges:
        st.subheader("🧗 Tantangan & Solusi")
        for i, challenge in enumerate(project.challenges, 1):
            st.markdown(f"**{i}.** {challenge}")
    
    # Outcomes / Key Takeaways (jika ada)
    if project.outcomes:
        st.subheader("✨ Hasil & Pembelajaran")
        for outcome in project.outcomes:
            st.markdown(f"• {outcome}")
    
    # Call to Action
    st.markdown("---")
    col_cta1, col_cta2, col_cta3 = st.columns(3)
    
    with col_cta1:
        if project.github_url:
            st.link_button("📦 Lihat Kode", project.github_url, use_container_width=True)
    
    with col_cta2:
        if is_internal_page and internal_page_path:
            if st.button("▶ Buka Demo", key=f"demo_{project.id}", use_container_width=True):
                st.switch_page(internal_page_path)
        elif project.demo_url:
            st.link_button("🚀 Coba Demo", project.demo_url, use_container_width=True)
    
    with col_cta3:
        if st.button("📤 Share Proyek", use_container_width=True):
            st.toast(f"Link proyek: {project.github_url or project.demo_url or 'N/A'}", icon="🔗")
