import streamlit as st

def main():
    st.title("👤 Tentang Saya")
    
    st.markdown("""
    Selamat datang di portofolio saya!  
    Aplikasi ini menampilkan informasi tentang diri saya, proyek-proyek yang pernah saya kerjakan, 
    serta implementasi machine learning untuk prediksi harga rumah.
    """)
    
    col1, col2 = st.columns([2, 3])
    
    with col1:
        st.image("https://via.placeholder.com/150?text=Foto", width=150)
        st.markdown("### 📋 Profil")
        st.markdown("**Nama:** Wandika Febriano Pangaribuan")
        st.markdown("**Role:** Senior Software Engineer")
        st.markdown("**Fokus:** Data Science & Machine Learning")
    
    with col2:
        st.markdown("### 🛠️ Keahlian")
        skills = {
            "Programming": ["Python", "SQL", "Bash"],
            "ML/DL": ["Scikit-learn", "TensorFlow", "PyTorch"],
            "Visualization": ["Matplotlib", "Seaborn", "Tableau", "Plotly"],
            "Tools": ["Streamlit", "Docker", "Git", "GCP"]
        }
        for category, items in skills.items():
            st.markdown(f"**{category}**")
            st.markdown(" • ".join(items))
            st.markdown("---")
    
    st.info("✨ Saya selalu bersemangat mengubah data menjadi insight berharga dan membangun solusi AI yang berdampak.")

if __name__ == "__main__":
    main()