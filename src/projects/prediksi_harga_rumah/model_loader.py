import pickle
import streamlit as st

@st.cache_resource
def load_model(model_path: str = 'src/projects/prediksi_harga_rumah/model.pkl'):
    """Load trained model from pickle file."""
    with open(model_path, 'rb') as f:
        return pickle.load(f)

@st.cache_resource
def load_eval_data(data_path: str = 'src/projects/prediksi_harga_rumah/eval_data.pkl'):
    """Load evaluation data from pickle file."""
    with open(data_path, 'rb') as f:
        return pickle.load(f)