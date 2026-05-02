FEATURE = [
    "OverallQual", "GrLivArea", "GarageCars", "GarageArea", "TotalBsmtSF", 
    "1stFlrSF", "FullBath", "TotRmsAbvGrd", "YearBuilt", "YearRemodAdd",
    "ExterQual", "KitchenQual", "BsmtQual", "GarageFinish", "Foundation", 
    "CentralAir", "Neighborhood", "GarageType", "BsmtExposure", "BsmtFinType1", 
    "SaleCondition", "MSZoning", "PavedDrive", "LotShape", "SaleType"
]

PROFILE = {
    "name": "Wandika Febriano Pangaribuan",
    "title": "Senior Software Engineer | AI Engineer",
    "tagline": "Software Engineer turned AI Engineer — building scalable systems and intelligent products with 6+ years of backend, microservices, and data-driven development experience.",
    "bio": (
        "I am a Software Engineer with over 6 years of experience designing and developing scalable web applications, backend systems, and cloud-based solutions across e-commerce, enterprise, and digital platforms. My technical foundation in Java, Spring Boot, microservices, APIs, databases, and Google Cloud Platform has allowed me to build reliable production systems at scale.",
        "Now, I am actively expanding into AI Engineering by combining my software architecture expertise with machine learning, data engineering, and modern AI technologies. My goal is to bridge robust software engineering with practical AI implementation — creating intelligent systems that are not only innovative, but production-ready, maintainable, and business-focused.",
        "I am seeking opportunities where I can contribute as an AI Engineer, Backend Engineer, or Cloud/ML Engineer, particularly in roles involving machine learning systems, cloud infrastructure, and scalable AI product development."
    ),
    "location": "Jakarta, Indonesia",
    "email": "wandika.pangaribuan@gmail.com",
    "availability": "Open to opportunities",
    "social": {
        "LinkedIn": {"url": "https://www.linkedin.com/in/wandika-pangaribuan/", "icon": "🔗"},
        "GitHub": {"url": "https://github.com/wandikafp", "icon": "💻"},
    },
}

METRICS = [
    ("6+", "Years of Experience"),
    ("10+", "Projects Completed"),
    ("3", "Major Companies"),
    ("3", "Industries")
]

EXPERIENCE = [
    {
        "company": "DBS Bank",
        "role": "Digibank Senior Software Engineer",
        "period": "2022 — Present",
        "description": [
            "Developed and maintained production-ready microservices for supporting critical banking operations",
            "Partnered with cross-functional teams to ensure high-quality feature delivery and strict adherence to organizational security standards",
            "Resolved high-impact technical issues, minimizing business downtime and ensuring continuous operational stability",
            "Conducted technical analysis and implementation planning, improving project delivery timelines by 20%",
        ],
        "tech": ["Java", "Spring Framework", "MariaDB", "Docker", "OpenShift (OCP)"],
    },
    {
        "company": "Blibli.com",
        "role": "Software Development Engineer",
        "period": "2021 — 2022",
        "description": [
            "Developed and maintained B2B affiliate services enabling business partners to transact via high-scale APIs",
            "Built internal B2B platforms for finance operations, achieving a 50% improvement in process efficiency through automation",
            "Enhanced service reliability and scalability by integrating asynchronous messaging and caching layers into microservice architectures",
        ],
        "tech": ["Vue.js", "Typescript", "Java", "Spring WebFlux", "MongoDB", "Kafka", "Redis", "Docker", "Kubernetes"],
    },
    {
        "company": "Xtremax",
        "role": "Software Developer",
        "period": "2018 — 2021",
        "description": [
            "Designed and maintained high-quality web applications for diverse enterprise clients",
            "Improved application stability and long-term maintainability by proactively refactoring legacy code modules",
            "Collaborated within Agile teams to deliver complex projects on schedule, consistently increasing client satisfaction",
        ],
        "tech": [".NET Core", "MSSQL Server", "MySQL", "PostgreSQL", "RabbitMQ", "Docker", "Vue.js", "Kubernetes"],
    },
]

SKILLS = {
    "⌨️ Programming": [
        "Java",
        "Python",
        "SQL",
        "NoSQL",
        "Bash",
        "JavaScript",
        "C#"
    ],

    "🤖 ML / AI": [
        "Scikit-learn",
        "TensorFlow",
        "PyTorch",
        "XGBoost",
        "LSTM",
        "BERT",
        "Machine Learning Fundamentals",
        "Data Processing",
        "RAG Concepts"
    ],

    "📊 Visualization": [
        "Plotly",
        "Matplotlib",
        "Seaborn",
        "Tableau",
        "Streamlit",
        "Dashboard Development"
    ],

    "⚙️ DevOps & Tools": [
        "Docker",
        "FastAPI",
        "Spring Boot",
        "Git",
        "GCP",
        "Redis",
        "Airflow",
        "REST APIs",
        "Microservices",
        "CI/CD"
    ]
}

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
        "demo_url": "__page__:pages/🏠_Prediksi_Harga_Rumah.py",
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
        "id": "customer-intelligence",
        "title": "🏦 SafeBank Customer Intelligence",
        "description": "Membangun sistem customer intelligence menggunakan NLP dan RAG untuk menganalisis sentimen pelanggan dan memberikan rekomendasi produk keuangan yang dipersonalisasi.",
        "long_description": """
        SafeBank Customer Intelligence adalah sistem berbasis AI yang dirancang untuk memberikan 
        wawasan mendalam tentang kepuasan dan preferensi pelanggan bank. Sistem ini 
        menggabungkan Natural Language Processing (NLP) dengan Retrieval-Augmented 
        Generation (RAG) untuk menganalisis feedback pelanggan dalam skala besar dan 
        memberikan rekomendasi produk yang dipersonalisasi.

        Key Features:
        🔹 **Customer Feedback Analysis**: Menganalisis ulasan, komentar, dan interaksi pelanggan 
        untuk mengidentifikasi tren, sentimen, dan masalah yang sering muncul
        🔹 **Personalized Product Recommendation**: Memberikan rekomendasi produk perbankan 
        yang disesuaikan dengan kebutuhan dan profil masing-masing pelanggan
        🔹 **Smart Q&A System**: Chatbot cerdas yang dapat menjawab pertanyaan pelanggan 
        secara akurat dengan memanfaatkan database pengetahuan internal bank
        🔹 **Customer Behavior Insights**: Mendeteksi pola perilaku pelanggan dan memberikan 
        peringatan dini jika ada potensi churn (perpindahan nasabah)
        
        Technical Architecture:
        🎯 **Embedding Model**: Sentence-Transformers untuk representasi semantik teks
        💾 **Vector Database**: PGVector untuk penyimpanan dan pencarian vektor yang efisien
        🧠 **LLM Integration**: Groq API untuk pemrosesan bahasa alami tingkat lanjut
        📊 **Frontend**: Streamlit untuk antarmuka pengguna yang interaktif
        📦 **Deployment**: Docker untuk kemudahan deployment dan skalabilitas
        """,
        "tools": ["Python", "PGVector", "Groq API", "Streamlit", "Docker", "Sentence-Transformers"],
        "image_url": "https://via.placeholder.com/600x300?text=Customer+Intelligence",
        "github_url": "",
        "demo_url": "__page__:pages/customer_intelligence.py",
        "metrics": {"Token": "1024", "Timeout": "None", "Max Retries": "3"},
        "challenges": [
            """
            RAG Implementation Challenges: Implementing Retrieval-Augmented Generation (RAG) presents 
            unique challenges compared to traditional NLP applications. One significant challenge is 
            optimizing the retrieval component to ensure relevant context is fetched for each query. 
            This involves fine-tuning the embedding model to understand domain-specific language and 
            experimenting with different chunking strategies to maximize retrieval accuracy.
            
            Scalability: As the volume of customer feedback grows, scaling the RAG system becomes critical. 
            Storing and efficiently querying millions of vectors requires a robust vector database solution 
            and careful optimization of indexing strategies. Additionally, managing API rate limits and 
            response times for the LLM integration while maintaining low latency can be complex.
            
            Evaluation and Validation: Evaluating the performance of a RAG system goes beyond 
            traditional accuracy metrics. It requires assessing both the quality of the retrieved context 
            and the relevance of the generated responses. Developing comprehensive evaluation frameworks 
            that measure factors like factual consistency, helpfulness, and domain appropriateness 
            is essential for ensuring the system meets business requirements.
            """
        ],
        "outcomes": [
            """
            Enhanced Customer Experience: The RAG-powered Q&A system significantly improves 
            customer satisfaction by providing instant, accurate answers to their queries. 
            Personalized product recommendations tailored to individual preferences help customers 
            find relevant products quickly, increasing engagement and conversion rates.
            
            Proactive Churn Prevention: By analyzing customer behavior patterns and feedback, 
            the system enables proactive intervention to prevent customer churn. Early detection of 
            dissatisfied customers allows the bank to address issues promptly and retain valuable 
            customers, ultimately protecting revenue streams.
            
            Operational Efficiency: Automating customer support through the chatbot reduces 
            the workload on human support agents, allowing them to focus on more complex 
            issues. This operational efficiency translates to cost savings and improved 
            service quality across the organization.
            """
        ]
    },
    {
        "id": "recommendation-system",
        "title": "🎬 Movie Recommendation System",
        "description": "Membangun sistem rekomendasi film hybrid menggunakan Content-Based Filtering, Collaborative Filtering (SVD), dan penggabungan keduanya untuk menghasilkan rekomendasi yang lebih akurat.",
        "long_description": """
        Proyek ini membangun dan mengevaluasi sistem rekomendasi film yang robust dengan mengeksplorasi
        berbagai strategi rekomendasi, lalu menggabungkannya menjadi Hybrid Recommendation System.
        
        Pipeline yang dibangun meliputi:
        
        1. **Data Preprocessing**: Memuat dataset film dan rating (MovieLens), menangani missing values pada kolom genres
        2. **Content-Based Filtering (CBF)**: Ekstraksi fitur menggunakan TF-IDF Vectorizer pada genre film, 
        menghitung kemiripan dengan Cosine Similarity dan Euclidean Distance
        3. **Collaborative Filtering (CF)**:
           - *Item-Based*: Membuat user-item matrix dan menghitung kemiripan antar item
           - *Model-Based (SVD)*: Melatih model Matrix Factorization menggunakan library `scikit-surprise`
        4. **Hybrid Recommendation System**: Menggabungkan skor dari CBF dan SVD dengan formula:
           `Hybrid Score = (0.4 × CBF_Score) + (0.6 × CF_Score)`
        5. **Evaluation**: Mengevaluasi performa model SVD menggunakan RMSE dan MAE
        
        Dataset: ~9.742 film dari dataset MovieLens (movies.csv & ratings.csv).
        """,
        "tools": ["Python", "Scikit-learn", "Scikit-surprise", "Pandas", "NumPy", "Matplotlib", "Seaborn"],
        "image_url": "https://via.placeholder.com/600x300?text=Customer+Intelligence",
        "github_url": "",
        "demo_url": "https://colab.research.google.com/drive/1FN-DSbu5gBe_BXwsqfxve7ebnujzZrTR",
        "metrics": {"RMSE": "0.8717", "MAE": "0.6688", "Data": "9.742 Film"},
        "challenges": [
            "Content-Based Filtering sangat bergantung pada kualitas metadata — hanya genre yang tersedia sehingga rekomendasi kurang beragam (low serendipity)",
            "Collaborative Filtering menghadapi Cold Start Problem untuk user/item baru",
            "Data sparsity pada user-item rating matrix mengurangi kualitas rekomendasi CF"
        ],
        "outcomes": [
            "Hybrid model terbukti paling efektif karena mengatasi kelemahan CBF (kurang variatif) dan CF (cold start/sparsity)",
            "Kualitas dan kepadatan data (deskripsi item yang lebih kaya, riwayat rating yang lebih banyak) sangat mempengaruhi akurasi sistem rekomendasi",
            "Cosine Similarity dan Euclidean Distance menghasilkan hasil serupa karena feature space genre yang relatif terbatas"
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