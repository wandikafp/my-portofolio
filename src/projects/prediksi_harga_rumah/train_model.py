# train_model.py
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split, learning_curve
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

FEATURE = [
    "OverallQual", "GrLivArea", "GarageCars", "GarageArea", "TotalBsmtSF", 
    "1stFlrSF", "FullBath", "TotRmsAbvGrd", "YearBuilt", "YearRemodAdd",
    "ExterQual", "KitchenQual", "BsmtQual", "GarageFinish", "Foundation", 
    "CentralAir", "Neighborhood", "GarageType", "BsmtExposure", "BsmtFinType1", 
    "SaleCondition", "MSZoning", "PavedDrive", "LotShape", "SaleType"
]

# Load data
df = pd.read_csv('data/train.csv')

# Pisahkan fitur dan target
X = df.drop(['Id', 'SalePrice'], axis=1)[FEATURE]
y = df['SalePrice']

# Identifikasi kolom numerik dan kategorikal
numeric_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_features = X.select_dtypes(include=['object']).columns.tolist()

# Preprocessing pipeline
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Model pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training
model.fit(X_train, y_train)

# Evaluasi
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'RMSE: {rmse:.2f}')
print(f'MAE: {mae:.2f}')
print(f'R2: {r2:.4f}')

# Simpan model dan preprocessor
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Simpan data evaluasi untuk visualisasi nanti
eval_data = {
    'rmse': rmse,
    'mae': mae,
    'r2': r2,
    'feature_names': X.columns.tolist(),
    'y_test': y_test.values,
    'y_pred': y_pred,
    'X_train': X_train,  # untuk learning curve kita butuh data latih
    'y_train': y_train
}
with open('eval_data.pkl', 'wb') as f:
    pickle.dump(eval_data, f)

print("Model dan data evaluasi berhasil disimpan.")