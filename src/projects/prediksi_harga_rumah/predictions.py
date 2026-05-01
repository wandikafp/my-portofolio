import pandas as pd
import streamlit as st

def preprocess_input(df: pd.DataFrame) -> pd.DataFrame:
    """Remove unnecessary columns before prediction."""
    df_clean = df.copy()
    for col in ['Id', 'SalePrice']:
        if col in df_clean.columns:
            df_clean = df_clean.drop(col, axis=1)
    return df_clean

def make_predictions(model, df: pd.DataFrame) -> pd.DataFrame:
    """Generate predictions and return formatted DataFrame."""
    df_processed = preprocess_input(df)
    predictions = model.predict(df_processed)
    return pd.DataFrame({'Prediksi Harga ($)': predictions})

def download_csv(df: pd.DataFrame, filename: str = 'prediksi_harga.csv'):
    """Return CSV data for download button."""
    csv = df.to_csv(index=False).encode('utf-8')
    return csv