import streamlit as st
import pandas as pd
from model.predictions import make_predictions, download_csv

def main():
    st.title("🏠 Prediksi Harga Rumah")
    st.markdown("""
    Unggah file CSV dengan fitur yang sesuai (seperti `train.csv` tanpa kolom `SalePrice`) 
    untuk mendapatkan prediksi harga.
    """)
    
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

if __name__ == "__main__":
    main()