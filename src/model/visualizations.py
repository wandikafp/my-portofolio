import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import learning_curve

def plot_distribution(df: pd.DataFrame, column: str, exclude: list = None):
    """Plot histogram for numeric column."""
    exclude = exclude or ['Id', 'SalePrice']
    if column in exclude or column not in df.select_dtypes(include=[np.number]).columns:
        return None
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df[column].dropna(), bins=30, edgecolor='black', alpha=0.7)
    ax.set_title(f'Distribusi {column}')
    ax.set_xlabel(column)
    ax.set_ylabel('Frekuensi')
    ax.grid(axis='y', alpha=0.3)
    return fig

def plot_correlation_matrix(df: pd.DataFrame, exclude: list = None):
    """Plot correlation heatmap for numeric columns."""
    exclude = exclude or ['Id']
    numeric_df = df.select_dtypes(include=[np.number]).drop(columns=exclude, errors='ignore')
    
    if numeric_df.empty:
        return None
    
    fig, ax = plt.subplots(figsize=(14, 10))
    corr = numeric_df.corr()
    sns.heatmap(corr, annot=False, cmap='coolwarm', center=0, ax=ax)
    ax.set_title('Matriks Korelasi Fitur Numerik')
    return fig

def plot_actual_vs_predicted(y_true, y_pred):
    """Plot actual vs predicted scatter plot."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(y_true, y_pred, alpha=0.5, edgecolors='k')
    min_val = min(y_true.min(), y_pred.min())
    max_val = max(y_true.max(), y_pred.max())
    ax.plot([min_val, max_val], [min_val, max_val], 'r--', lw=2, label='Perfect Prediction')
    ax.set_xlabel('Actual Price')
    ax.set_ylabel('Predicted Price')
    ax.set_title('Actual vs Predicted')
    ax.legend()
    ax.grid(True, alpha=0.3)
    return fig

def plot_learning_curve(model, X_train, y_train, cv=5):
    """Compute and plot learning curve."""
    train_sizes = np.linspace(0.1, 1.0, 10)
    train_scores, test_scores = learning_curve(
        model, X_train, y_train, cv=cv,
        scoring='neg_root_mean_squared_error',
        n_jobs=-1, train_sizes=train_sizes, random_state=42
    )
    
    train_errors = -train_scores.mean(axis=1)
    test_errors = -test_scores.mean(axis=1)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(train_sizes, train_errors, 'o-', label='Training Error', linewidth=2)
    ax.plot(train_sizes, test_errors, 's-', label='Validation Error', linewidth=2)
    ax.set_xlabel('Jumlah Data Latih')
    ax.set_ylabel('RMSE')
    ax.set_title('Learning Curve')
    ax.legend()
    ax.grid(True, alpha=0.3)
    return fig