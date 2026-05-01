FEATURE = [
    "OverallQual", "GrLivArea", "GarageCars", "GarageArea", "TotalBsmtSF", 
    "1stFlrSF", "FullBath", "TotRmsAbvGrd", "YearBuilt", "YearRemodAdd",
    "ExterQual", "KitchenQual", "BsmtQual", "GarageFinish", "Foundation", 
    "CentralAir", "Neighborhood", "GarageType", "BsmtExposure", "BsmtFinType1", 
    "SaleCondition", "MSZoning", "PavedDrive", "LotShape", "SaleType"
]

PROJECTS = [
    {
        "id": "house-price-prediction",
        "title": "🏠 Prediksi Harga Rumah (House Prices)",
        "description": "Pipeline machine learning end-to-end untuk memprediksi harga rumah dengan Random Forest. RMSE 0.15 (standarisasi).",
        "long_description": """
        Sistem prediksi harga rumah berbasis machine learning dengan fitur:
        
        🔹 **Data Pipeline**: Automated ETL dari CSV/JSON, handling missing values
        🔹 **Feature Engineering**: Polynomial features, interaction terms, encoding
        
        Deploy sebagai REST API dengan FastAPI + Docker.
        """,
        "tools": ["Scikit-learn", "Pandas", "Streamlit", "Docker"],
        "image_url": "https://via.placeholder.com/600x300?text=House+Price+Prediction",
        "github_url": "https://github.com/wandikafp",
        "demo_url": "",
        "metrics": {"RMSE": "0.15", "R²": "0.89", "Fitur": "80+"},
        "challenges": [
            "Feature selection dari 300+ kolom awal",
            "Handling outliers pada harga properti ekstrem",
            "Model serialization untuk deployment yang efisien"
        ],
        "outcomes": [
            "Template pipeline ML untuk regression problems",
            "Monitoring dashboard untuk model drift detection",
            "Cost optimization: 70% lebih hemat dengan model pruning"
        ]
    },
    {
        "id": "sentiment-analysis",
        "title": "📊 Analisis Sentimen Ulasan Produk",
        "description": "Menganalisis sentimen ulasan produk e-commerce menggunakan NLP dan model LSTM. Mencapai akurasi 92%.",
        "long_description": """
        Proyek ini bertujuan untuk mengklasifikasikan sentimen pelanggan dari ulasan produk 
        e-commerce secara otomatis. Pipeline yang dibangun meliputi:
        
        1. **Data Collection & Preprocessing**: Scraping ulasan, cleaning text, tokenization
        2. **Feature Engineering**: TF-IDF, Word2Vec embeddings
        3. **Modeling**: LSTM dengan TensorFlow, perbandingan dengan BERT fine-tuning
        4. **Evaluation**: Cross-validation, confusion matrix, classification report
        
        Model akhir mencapai **akurasi 92%** dengan F1-score 0.91 pada kelas minoritas.
        """,
        "tools": ["Python", "TensorFlow", "NLTK", "Streamlit", "Docker"],
        "image_url": "https://via.placeholder.com/600x300?text=Sentiment+Analysis",
        "github_url": "https://github.com/wandikafp",
        "demo_url": "https://sentiment-demo.streamlit.app",
        "metrics": {"Akurasi": "92%", "F1-Score": "0.91", "Data": "50K+ ulasan"},
        "challenges": [
            "Handling imbalanced classes dengan SMOTE",
            "Optimasi hyperparameter LSTM untuk training time yang efisien",
            "Deploy model dengan Docker untuk konsistensi environment"
        ],
        "outcomes": [
            "Pipeline NLP reusable untuk proyek serupa",
            "Dokumentasi lengkap untuk reproducibility",
            "Integration dengan API untuk real-time prediction"
        ]
    },
    {
        "id": "covid-dashboard",
        "title": "📈 Dashboard COVID-19 Interaktif",
        "description": "Dashboard interaktif yang menampilkan perkembangan kasus COVID-19 global dengan berbagai filter dan visualisasi real-time.",
        "long_description": """
        Dashboard analitik untuk monitoring pandemi COVID-19 dengan kemampuan:
        
        🌍 **Global & Regional Views**: Filter by country, date range, metrics
        📊 **Interactive Charts**: Time series, choropleth maps, comparative analysis
        ⚡ **Real-time Updates**: Auto-refresh dari WHO/Johns Hopkins API
        📱 **Responsive Design**: Mobile-friendly dengan Plotly Dash
        
        Dibangun dengan arsitektur serverless untuk skalabilitas tinggi.
        """,
        "tools": ["Plotly Dash", "Pandas", "Heroku", "Google Sheets API", "Redis"],
        "image_url": "https://via.placeholder.com/600x300?text=COVID+Dashboard",
        "github_url": "https://github.com/wandikafp",
        "demo_url": "https://covid-dashboard-demo.herokuapp.com",
        "metrics": {"Users": "10K+", "Uptime": "99.9%", "Latency": "<200ms"},
        "challenges": [
            "Rate limiting dan caching untuk API eksternal",
            "Optimasi rendering untuk dataset besar (1M+ rows)",
            "Multi-language support untuk akses global"
        ],
        "outcomes": [
            "Pattern untuk real-time data visualization apps",
            "Best practices untuk dashboard performance optimization",
            "Reusable components library untuk Plotly Dash"
        ]
    }
]