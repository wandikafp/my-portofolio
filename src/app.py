import streamlit as st

# ── Define navigation — hanya halaman yang listed yang tampil di sidebar ──
home_page    = st.Page("pages/1_🏠_Home.py", title="Home", icon="🏠", default=True)
proyek_page  = st.Page("pages/2_💼_Projects.py", title="Proyek Saya", icon="💼")

# Prediksi diakses via demo button, tidak tampil di sidebar nav utama
prediksi_page = st.Page("pages/🏠_Prediksi_Harga_Rumah.py", title="Prediksi Harga Rumah")

chatbot_page = st.Page("pages/customer_intelligence.py", title="SafeBank Assistant", icon="🏦")

pg = st.navigation(
    {"": [home_page, proyek_page], "Demo": [prediksi_page, chatbot_page]},
    position="sidebar"
)

# Sidebar extra content
with st.sidebar:
    st.markdown("---")

# Sembunyikan section kedua (prediksi) dari tampilan sidebar
st.markdown("""
<style>
/* Sembunyikan section separator + item prediksi dari sidebar */
[data-testid="stSidebarNavSeparator"] ~ ul { display: none !important; }
[data-testid="stSidebarNavSeparator"]       { display: none !important; }
</style>
""", unsafe_allow_html=True)

pg.run()