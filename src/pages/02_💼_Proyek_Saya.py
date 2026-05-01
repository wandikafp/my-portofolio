from dto.Project import Project
import streamlit as st
from utils.config import PROJECTS
from typing import Optional
from components.project_card import render_project_card
from components.project_detail import render_project_detail

def get_project_by_id(projects: list[Project], project_id: str) -> Optional[dict]:
    """Helper function untuk mencari project berdasarkan ID."""
    return next((p for p in projects if p.id == project_id), None)

def main():
    st.title("💼 Proyek Saya")
    st.markdown("Berikut adalah beberapa proyek unggulan yang pernah saya selesaikan.")

    projects_data = [Project(**data) for data in PROJECTS]
    
    # Check jika ada project_id di query params (navigasi langsung)
    if "project" in st.query_params:
        project_id = st.query_params["project"]
        project = get_project_by_id(projects_data, project_id)
        
        if project:
            # Render detail jika project ditemukan
            render_project_detail(project)
            return
        else:
            st.warning(f"⚠️ Proyek dengan ID '{project_id}' tidak ditemukan.")
            st.query_params.pop("project", None)
    
    # Render List Project Cards
    for project in projects_data:
        render_project_card(project, key_prefix="projects_list")
    
    # Footer
    st.markdown("---")
    st.caption("💡 Klik *'Lihat Detail'* pada proyek untuk informasi lengkap.")

if __name__ == "__main__":
    main()