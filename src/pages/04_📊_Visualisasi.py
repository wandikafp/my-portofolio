import streamlit as st
import pandas as pd
from model.visualizations import (
    plot_distribution, 
    plot_correlation_matrix, 
    plot_actual_vs_predicted, 
    plot_learning_curve
)

def main():
    st.title("📊 Visualisasi Model & Data")
    st.markdown("Eksplorasi dataset dan performa model machine learning.")
    
    if not st.session_state.get("model_loaded", False):
        st.error("⚠️ Model dan data evaluasi belum tersedia. Jalankan `train_model.py` terlebih dahulu.")
        return
    
    # Load original dataset for visualization
    try:
        df = pd.read_csv('data/train.csv')
    except FileNotFoundError:
        st.warning("⚠️ File `data/train.csv` tidak ditemukan. Beberapa visualisasi mungkin tidak tersedia.")
        df = None
    
    eval_data = st.session_state.eval_data
    model = st.session_state.model
    
    # Visualization selector
    viz_option = st.selectbox(
        "🔍 Pilih jenis visualisasi",
        ["Distribusi Fitur", "Korelasi Fitur", "Metrik Performa", "Learning Curve"]
    )
    
    # ─── Distribusi Fitur ──────────────────────────────────────
    if viz_option == "Distribusi Fitur":
        st.subheader("📈 Distribusi Fitur Numerik")
        if df is not None:
            numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
            plot_cols = [col for col in numeric_cols if col not in ['Id', 'SalePrice']]
            
            if plot_cols:
                selected_col = st.selectbox("Pilih fitur", plot_cols)
                fig = plot_distribution(df, selected_col)
                if fig:
                    st.pyplot(fig)
            else:
                st.warning("Tidak ada kolom numerik untuk ditampilkan.")
        else:
            st.info("ℹ️ Load dataset `data/train.csv` untuk melihat distribusi fitur.")
    
    # ─── Korelasi Fitur ────────────────────────────────────────
    elif viz_option == "Korelasi Fitur":
        st.subheader("🔗 Matriks Korelasi Fitur Numerik")
        if df is not None:
            fig = plot_correlation_matrix(df)
            if fig:
                st.pyplot(fig)
        else:
            st.info("ℹ️ Load dataset `data/train.csv` untuk melihat korelasi fitur.")
    
    # ─── Metrik Performa ───────────────────────────────────────
    elif viz_option == "Metrik Performa":
        st.subheader("🎯 Performa Model (Data Uji)")
        
        # Metrics cards
        col1, col2, col3 = st.columns(3)
        col1.metric("RMSE", f"{eval_data['rmse']:.4f}")
        col2.metric("MAE", f"{eval_data['mae']:.4f}")
        col3.metric("R²", f"{eval_data['r2']:.4f}")
        
        # Actual vs Predicted plot
        st.markdown("### 🔍 Actual vs Predicted")
        fig = plot_actual_vs_predicted(eval_data['y_test'], eval_data['y_pred'])
        st.pyplot(fig)
    
    # ─── Learning Curve ────────────────────────────────────────
    elif viz_option == "Learning Curve":
        st.subheader("📉 Learning Curve")
        st.markdown("Menampilkan error training dan validasi seiring bertambahnya jumlah data latih.")
        
        with st.spinner("Menghitung learning curve..."):
            fig = plot_learning_curve(
                model, 
                eval_data['X_train'], 
                eval_data['y_train']
            )
        st.pyplot(fig)
    
    # ─── Sidebar Info ─────────────────────────────────────────
    with st.sidebar:
        st.markdown("---")
        st.markdown("### ℹ️ Info Model")
        st.code("Random Forest Regressor", language="python")
        st.markdown(f"- **Fitur:** {eval_data.get('n_features', 'N/A')}")
        st.markdown(f"- **Data Latih:** {eval_data.get('train_size', 'N/A')} sampel")

if __name__ == "__main__":
    main()