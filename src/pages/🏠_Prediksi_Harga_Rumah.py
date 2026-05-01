import streamlit as st
import pandas as pd
from projects.prediksi_harga_rumah.predictions import make_predictions, download_csv
from projects.prediksi_harga_rumah.model_loader import load_model, load_eval_data
from components.visualisasi_harga_rumah import visualisasi_harga_rumah

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

def main():
    st.title("🏠 Prediksi Harga Rumah")
    st.markdown("""
    Unggah file CSV dengan fitur yang sesuai (seperti `train.csv` tanpa kolom `SalePrice`) 
    untuk mendapatkan prediksi harga.
    """)

    with st.sidebar:
        st.markdown("### 📦 Status Model")
        if st.session_state.get("model_loaded"):
            st.success("✅ Model siap digunakan")
        else:
            st.error("❌ Model tidak ditemukan")
            st.caption(f"`{st.session_state.get('load_error', '')}`")
    
    # Check model availability
    if not st.session_state.get("model_loaded", False):
        st.error("⚠️ Model belum tersedia. Pastikan Anda telah menjalankan `train_model.py` untuk menghasilkan model.")
        return
    
    model = st.session_state.model
    
    uploaded_file = st.file_uploader("📁 Pilih file CSV", type="csv")
    
    if uploaded_file is not None:
        try:
            input_df = pd.read_csv(uploaded_file)
            
            with st.expander("🔍 Pratinjau Data", expanded=False):
                st.dataframe(input_df.head())
                st.markdown(f"**Dimensi:** {input_df.shape[0]} baris × {input_df.shape[1]} kolom")
            
            if st.button("🚀 Jalankan Prediksi", type="primary"):
                with st.spinner("Sedang memproses prediksi..."):
                    result_df = make_predictions(model, input_df)
                    
                st.success("✅ Prediksi berhasil!")
                st.dataframe(result_df.style.format({'Prediksi Harga ($)': '${:,.2f}'}))
                
                # Download button
                csv = download_csv(result_df)
                st.download_button(
                    label="📥 Unduh Hasil Prediksi (CSV)",
                    data=csv,
                    file_name='prediksi_harga.csv',
                    mime='text/csv',
                )
                
        except Exception as e:
            st.error(f"❌ Terjadi kesalahan: {str(e)}")
            st.exception(e)  # Untuk debugging di development
    
    visualisasi_harga_rumah()

if __name__ == "__main__":
    main()