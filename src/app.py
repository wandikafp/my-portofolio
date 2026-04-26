# app.py
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import learning_curve
from sklearn.metrics import mean_squared_error
from io import BytesIO

# ---------- Page Config ----------
st.set_page_config(page_title="My Portfolio", layout="wide")

# ---------- Load Model & Data ----------
@st.cache_resource
def load_model():
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

@st.cache_resource
def load_eval_data():
    with open('eval_data.pkl', 'rb') as f:
        data = pickle.load(f)
    return data

try:
    model = load_model()
    eval_data = load_eval_data()
    model_loaded = True
except FileNotFoundError:
    model_loaded = False

# ---------- Sidebar Navigation ----------
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman", ["Tentang Saya", "Proyek Saya", "Prediksi Harga Rumah", "Visualisasi Model & Data"])

# ---------- Page: Tentang Saya ----------
if page == "Tentang Saya":
    st.title("My Portfolio with Streamlit")
    st.markdown("""
    Selamat datang di portofolio saya!  
    Aplikasi ini menampilkan informasi tentang diri saya, proyek-proyek yang pernah saya kerjakan, 
    serta implementasi machine learning untuk prediksi harga rumah.
    """)

    st.header("Tentang Saya")
    st.markdown("**Nama:** Wandika Febriano Pangaribuan")
    st.markdown("**Latar Belakang:** Senior Software Engineer dengan minat di bidang Data Science dan Machine Learning.")
    st.markdown("**Keahlian:** Python, SQL, Machine Learning (Scikit-learn, TensorFlow), Data Visualization (Matplotlib, Seaborn, Tableau), Streamlit, Git.")

    # Tambahan elemen teks
    st.info("Saya selalu bersemangat mengubah data menjadi insight berharga dan membangun solusi AI yang berdampak.")

# ---------- Page: Proyek Saya ----------
elif page == "Proyek Saya":
    st.title("Proyek Saya")
    st.markdown("Berikut adalah beberapa proyek unggulan yang pernah saya selesaikan.")

    # Proyek 1
    with st.expander("📊 Analisis Sentimen Ulasan Produk", expanded=True):
        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown("**Deskripsi:** Menganalisis sentimen ulasan produk e-commerce menggunakan NLP dan model LSTM. Mencapai akurasi 92%.")
            st.markdown("**Tools:** Python, TensorFlow, NLTK, Streamlit, Docker.")
        with col2:
            st.image("https://via.placeholder.com/400x200?text=Sentiment+Analysis", use_column_width=True)

    # Proyek 2
    with st.expander("🏠 Prediksi Harga Rumah (House Prices)", expanded=False):
        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown("**Deskripsi:** Pipeline machine learning end-to-end untuk memprediksi harga rumah dengan Random Forest. RMSE 0.15 (standarisasi).")
            st.markdown("**Tools:** Scikit-learn, Pandas, Streamlit, Docker, GCP Cloud Run.")
        with col2:
            st.image("https://via.placeholder.com/400x200?text=House+Price+Prediction", use_column_width=True)

    # Proyek 3
    with st.expander("📈 Dashboard COVID-19", expanded=False):
        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown("**Deskripsi:** Dashboard interaktif yang menampilkan perkembangan kasus COVID-19 global dengan berbagai filter.")
            st.markdown("**Tools:** Plotly Dash, Pandas, Heroku, Google Sheets API.")
        with col2:
            st.image("https://via.placeholder.com/400x200?text=COVID+Dashboard", use_column_width=True)

    st.caption("Klik setiap proyek untuk melihat detail. Gambar hanya ilustrasi.")

# ---------- Page: Prediksi Harga Rumah ----------
elif page == "Prediksi Harga Rumah":
    st.title("Implementasi Prediksi Harga Rumah")
    st.markdown("Unggah file CSV dengan fitur yang sesuai (seperti `train.csv` tanpa kolom `SalePrice`) untuk mendapatkan prediksi harga.")

    if not model_loaded:
        st.error("Model belum tersedia. Pastikan Anda telah menjalankan `train_model.py` untuk menghasilkan model.")
    else:
        uploaded_file = st.file_uploader("Pilih file CSV", type="csv")
        if uploaded_file is not None:
            try:
                input_df = pd.read_csv(uploaded_file)
                st.write("Pratinjau data yang diunggah:")
                st.dataframe(input_df.head())

                # Tombol prediksi
                if st.button("Prediksi Harga"):
                    # Pastikan tidak ada kolom Id atau SalePrice (akan diabaikan)
                    if 'Id' in input_df.columns:
                        input_df = input_df.drop('Id', axis=1)
                    if 'SalePrice' in input_df.columns:
                        input_df = input_df.drop('SalePrice', axis=1)

                    predictions = model.predict(input_df)
                    result_df = pd.DataFrame({'Prediksi Harga ($)': predictions})
                    st.success("Prediksi berhasil!")
                    st.dataframe(result_df)

                    # Download hasil
                    csv = result_df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="Unduh Hasil Prediksi (CSV)",
                        data=csv,
                        file_name='prediksi_harga.csv',
                        mime='text/csv',
                    )
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")

# ---------- Page: Visualisasi Model & Data ----------
elif page == "Visualisasi Model & Data":
    st.title("Visualisasi Model & Data")
    st.markdown("Eksplorasi dataset dan performa model machine learning.")

    if not model_loaded:
        st.error("Model dan data evaluasi belum tersedia. Jalankan `train_model.py` terlebih dahulu.")
    else:
        # Load dataset asli untuk visualisasi distribusi
        df = pd.read_csv('data/train.csv')

        # Pilihan visualisasi
        viz_option = st.selectbox(
            "Pilih jenis visualisasi",
            ["Distribusi Fitur", "Korelasi Fitur", "Metrik Performa", "Learning Curve"]
        )

        if viz_option == "Distribusi Fitur":
            st.subheader("Distribusi Fitur Numerik")
            numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
            # Kecualikan Id dan SalePrice
            plot_cols = [col for col in numeric_cols if col not in ['Id', 'SalePrice']]
            if plot_cols:
                selected_col = st.selectbox("Pilih fitur", plot_cols)
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.hist(df[selected_col].dropna(), bins=30, edgecolor='black')
                ax.set_title(f'Distribusi {selected_col}')
                ax.set_xlabel(selected_col)
                ax.set_ylabel('Frekuensi')
                st.pyplot(fig)
                plt.close()
            else:
                st.warning("Tidak ada kolom numerik untuk ditampilkan.")

        elif viz_option == "Korelasi Fitur":
            st.subheader("Matriks Korelasi Fitur Numerik")
            numeric_df = df.select_dtypes(include=['int64', 'float64']).drop(['Id'], axis=1, errors='ignore')
            if not numeric_df.empty:
                corr = numeric_df.corr()
                fig, ax = plt.subplots(figsize=(14, 10))
                sns.heatmap(corr, annot=False, cmap='coolwarm', ax=ax)
                ax.set_title('Korelasi antar Fitur Numerik')
                st.pyplot(fig)
                plt.close()
            else:
                st.warning("Data tidak cukup untuk menghitung korelasi.")

        elif viz_option == "Metrik Performa":
            st.subheader("Performa Model (Data Uji)")
            metrics = {
                'RMSE': eval_data['rmse'],
                'MAE': eval_data['mae'],
                'R²': eval_data['r2']
            }
            col1, col2, col3 = st.columns(3)
            col1.metric("RMSE", f"{metrics['RMSE']:.4f}")
            col2.metric("MAE", f"{metrics['MAE']:.4f}")
            col3.metric("R²", f"{metrics['R²']:.4f}")

            # Visualisasi perbandingan actual vs predicted (opsional)
            st.markdown("**Actual vs Predicted**")
            fig, ax = plt.subplots()
            ax.scatter(eval_data['y_test'], eval_data['y_pred'], alpha=0.5)
            ax.plot([min(eval_data['y_test']), max(eval_data['y_test'])],
                    [min(eval_data['y_test']), max(eval_data['y_test'])], 'r--')
            ax.set_xlabel('Actual')
            ax.set_ylabel('Predicted')
            ax.set_title('Actual vs Predicted')
            st.pyplot(fig)
            plt.close()

        elif viz_option == "Learning Curve":
            st.subheader("Learning Curve")
            st.markdown("Menampilkan error training dan validasi seiring bertambahnya jumlah data latih.")
            # Hitung learning curve jika belum ada
            if 'learning_curve' not in eval_data:
                # Hitung learning curve
                train_sizes, train_scores, test_scores = learning_curve(
                    model, eval_data['X_train'], eval_data['y_train'], cv=5,
                    scoring='neg_root_mean_squared_error', n_jobs=-1,
                    train_sizes=np.linspace(0.1, 1.0, 10)
                )
                train_errors = -train_scores.mean(axis=1)
                test_errors = -test_scores.mean(axis=1)
                # Simpan sementara di eval_data (tidak permanen ke file)
                eval_data['train_errors'] = train_errors
                eval_data['test_errors'] = test_errors
                eval_data['train_sizes'] = train_sizes

            fig, ax = plt.subplots()
            ax.plot(eval_data['train_sizes'], eval_data['train_errors'], 'o-', label='Training error')
            ax.plot(eval_data['train_sizes'], eval_data['test_errors'], 'o-', label='Validation error')
            ax.set_xlabel('Jumlah data latih')
            ax.set_ylabel('RMSE')
            ax.set_title('Learning Curve')
            ax.legend()
            st.pyplot(fig)
            plt.close()

        # Opsi interaktif pilih model (kita hanya punya satu model, tapi bisa ditambahkan)
        st.sidebar.markdown("---")
        st.sidebar.caption("Model yang tersedia: Random Forest (default)")