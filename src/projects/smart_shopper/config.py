import os
import certifi
import streamlit as st
from pymongo import MongoClient
from google import genai
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

@st.cache_resource
def get_database_connection():
    mongo_uri = os.environ.get("MONGO_CONNECTION_STRING")
    ca = certifi.where()
    client = MongoClient(mongo_uri, tlsCAFile=ca)
    return client['smart_shopper_db']

@st.cache_resource
def get_embedding_model():
    return SentenceTransformer('all-mpnet-base-v2')

@st.cache_resource
def get_agent_client():
    return genai.Client() # Automatically picks up GEMINI_API_KEY from environment
