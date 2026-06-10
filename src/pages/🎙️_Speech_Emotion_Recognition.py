"""
Minimal Speech Emotion Recognition Demo
This is a single-file Streamlit application that you can easily copy to other projects.
Includes features for File Upload, Live Recording, and Contact Center Simulation.
"""

import os
import io
import numpy as np
import joblib
import librosa
import streamlit as st
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# ── Constants ─────────────────────────────────────────────────────────────────
TARGET_SR    = 22050
DURATION     = 3.0                     # seconds
N_SAMPLES    = int(TARGET_SR * DURATION)

FRAME_LENGTH = int(0.025 * TARGET_SR)  # 25 ms
HOP_LENGTH   = int(0.010 * TARGET_SR)  # 10 ms
N_FFT        = 2048

N_MFCC       = 13
MAX_FRAMES   = 400
N_FEATURES   = N_MFCC * 3 + 1         # 40

# ── Model Definition ─────────────────────────────────────────────────────────

@keras.utils.register_keras_serializable()
class SoftAttention(layers.Layer):
    """Soft attention mechanism for the model."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self, input_shape):
        self.W = self.add_weight(
            name="attention_weight",
            shape=(input_shape[-1],),
            initializer="glorot_uniform",
            trainable=True,
        )
        super().build(input_shape)

    def call(self, encoder_output):
        score   = tf.nn.tanh(encoder_output * self.W)
        score   = tf.reduce_sum(score, axis=-1, keepdims=True)
        weights = tf.nn.softmax(score, axis=1)
        context = tf.reduce_sum(weights * encoder_output, axis=1)
        return context, weights

    def get_config(self):
        return super().get_config()

# ── Feature Extraction ────────────────────────────────────────────────────────

def preprocess_audio(y: np.ndarray, sr: int) -> np.ndarray:
    """Resample, pre-emphasise, trim silence, and fix length."""
    if sr != TARGET_SR:
        y = librosa.resample(y, orig_sr=sr, target_sr=TARGET_SR)
    
    y = librosa.effects.preemphasis(y, coef=0.97)
    y, _ = librosa.effects.trim(y, top_db=30)
    
    if len(y) > N_SAMPLES:
        y = y[:N_SAMPLES]
    else:
        y = np.pad(y, (0, N_SAMPLES - len(y)), mode="constant")
    return y

def extract_features(y: np.ndarray) -> np.ndarray:
    """Extract MFCC + Delta + Delta-Delta + RMSE features."""
    mfcc = librosa.feature.mfcc(
        y=y, sr=TARGET_SR, n_mfcc=N_MFCC,
        n_fft=N_FFT, hop_length=HOP_LENGTH, win_length=FRAME_LENGTH,
    )
    delta = librosa.feature.delta(mfcc, width=9)
    delta2 = librosa.feature.delta(mfcc, order=2, width=9)
    rmse = librosa.feature.rms(
        y=y, frame_length=FRAME_LENGTH, hop_length=HOP_LENGTH
    )
    
    T_mfcc = mfcc.shape[1]
    if rmse.shape[1] > T_mfcc:
        rmse = rmse[:, :T_mfcc]
    elif rmse.shape[1] < T_mfcc:
        rmse = np.pad(rmse, ((0, 0), (0, T_mfcc - rmse.shape[1])), mode="edge")
        
    features = np.concatenate([mfcc, delta, delta2, rmse], axis=0).T
    
    T = features.shape[0]
    if T >= MAX_FRAMES:
        features = features[:MAX_FRAMES, :]
    else:
        pad = np.zeros((MAX_FRAMES - T, N_FEATURES), dtype=np.float32)
        features = np.vstack([features, pad])
        
    return features.astype(np.float32)

# ── Inference Engine ─────────────────────────────────────────────────────────

class SERPredictor:
    def __init__(self, model_path: str, scaler_path: str, encoder_path: str):
        self.model = keras.models.load_model(model_path, custom_objects={'SoftAttention': SoftAttention})
        self.scaler = joblib.load(scaler_path)
        encoder = joblib.load(encoder_path)
        self.label2idx = encoder["label2idx"]
        self.idx2label = encoder.get("idx2label", {v: k for k, v in self.label2idx.items()})
        self.classes = [self.idx2label[i] for i in range(len(self.idx2label))]

    def predict_from_array(self, audio: np.ndarray, sr: int) -> dict:
        y = preprocess_audio(audio, sr)
        feat = extract_features(y)
        
        # Normalize
        normed = self.scaler.transform(feat).astype(np.float32)
        X = normed[np.newaxis, ...]
        
        prob = self.model.predict(X, verbose=0)[0]
        dominant_idx = int(np.argmax(prob))
        
        emotion_scores = {cls: float(prob[i]) for i, cls in enumerate(self.classes)}
        return {
            "dominant_emotion": self.idx2label[dominant_idx],
            "confidence": float(prob[dominant_idx]),
            "emotion_scores": emotion_scores,
        }

# ── Contact Center Routing Logic ──────────────────────────────────────────────

def get_routing_action(emotion: str) -> dict:
    emotion = emotion.lower()
    if emotion in ['angry', 'disgust', 'fearful']:
        return {
            "priority": "🔴 TINGGI (Eskalasi)",
            "route_to": "Senior Escalation Agent",
            "handling_advice": "Pelanggan terdengar frustrasi/marah. Dengarkan dengan empati, jangan berdebat, dan tawarkan solusi segera."
        }
    elif emotion in ['sad']:
        return {
            "priority": "🟠 MENENGAH",
            "route_to": "Customer Retention / Empathy Agent",
            "handling_advice": "Pelanggan mungkin sedang kecewa atau sedih. Gunakan nada bicara yang lembut dan simpatik."
        }
    else:
        # neutral, calm, happy, surprised
        return {
            "priority": "🟢 NORMAL",
            "route_to": "Standard Support Agent",
            "handling_advice": "Sapa pelanggan dengan ramah dan profesional. Tangani permintaan sesuai prosedur standar."
        }

# ── Streamlit UI ──────────────────────────────────────────────────────────────

st.set_page_config(page_title="SER Demo", page_icon="🎙️", layout="wide")
st.title("🎙️ Speech Emotion Recognition Demo")
st.markdown("A minimal standalone demo for predicting emotion from audio, featuring **File Upload**, **Live Recording**, and **Contact Center Simulation**.")

# User needs to put these files in the same folder or update paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, "projects", "speech_emotion_recognition")

MODEL_PATH = os.path.join(PROJECT_DIR, "baseline_random_best.keras")
SCALER_PATH = os.path.join(PROJECT_DIR, "scaler.pkl")
ENCODER_PATH = os.path.join(PROJECT_DIR, "label_encoder.pkl")

@st.cache_resource
def load_system():
    if not all(os.path.exists(p) for p in [MODEL_PATH, SCALER_PATH, ENCODER_PATH]):
        return None
    return SERPredictor(MODEL_PATH, SCALER_PATH, ENCODER_PATH)

predictor = load_system()

if not predictor:
    st.error(f"Missing required files! Please ensure `{MODEL_PATH}`, `{SCALER_PATH}`, and `{ENCODER_PATH}` are in the same folder as this script.")
    st.stop()

st.success("✅ System ready. Choose an input method below.")

tab1, tab2, tab3 = st.tabs(["📁 Upload Audio", "🎤 Live Recording", "🎧 Contact Center Simulation"])

def display_prediction(result, col):
    with col:
        st.subheader(f"Predicted: {result['dominant_emotion'].title()} ({(result['confidence']*100):.1f}%)")
        st.markdown("**All Emotion Scores:**")
        sorted_scores = sorted(result['emotion_scores'].items(), key=lambda x: x[1], reverse=True)
        for emotion, score in sorted_scores:
            st.progress(score, text=f"{emotion.title()}: {score:.3f}")

# ── TAB 1: File Upload ────────────────────────────────────────────────────────
with tab1:
    uploaded_file = st.file_uploader("Upload Audio (WAV/MP3/OGG)", type=['wav', 'mp3', 'ogg'], key="upload")
    if uploaded_file is not None:
        st.audio(uploaded_file)
        if st.button("Predict Emotion from File", type="primary", key="btn_upload"):
            with st.spinner("Analyzing audio..."):
                try:
                    audio_bytes = uploaded_file.read()
                    y, sr = librosa.load(io.BytesIO(audio_bytes), sr=None, mono=True)
                    result = predictor.predict_from_array(y, sr)
                    display_prediction(result, st.container())
                except Exception as e:
                    st.error(f"Error during prediction: {e}")

# ── TAB 2: Live Recording ─────────────────────────────────────────────────────
with tab2:
    st.markdown("Click the microphone icon below to start recording. Speak for a few seconds to let the model capture your emotion.")
    audio_value = st.audio_input("Record your voice")
    
    if audio_value is not None:
        if st.button("Predict Emotion from Recording", type="primary", key="btn_record"):
            with st.spinner("Analyzing live recording..."):
                try:
                    audio_bytes = audio_value.read()
                    y, sr = librosa.load(io.BytesIO(audio_bytes), sr=None, mono=True)
                    result = predictor.predict_from_array(y, sr)
                    display_prediction(result, st.container())
                except Exception as e:
                    st.error(f"Error during prediction: {e}")

# ── TAB 3: Contact Center Simulation ──────────────────────────────────────────
with tab3:
    st.markdown("### 🎧 Simulasi Routing Telepon Pelanggan")
    st.info("Simulasikan penelepon (customer) yang sedang menghubungi customer service. Sistem akan mendeteksi emosi dari suaranya dan memberikan instruksi prioritas antrean serta rekomendasi penanganan kepada agen.")
    
    cc_audio = st.audio_input("Rekam Suara Pelanggan (Simulasi)")
    
    if cc_audio is not None:
        if st.button("Analisis Panggilan Masuk", type="primary", key="btn_cc"):
            with st.spinner("Menghubungkan ke AI Routing System..."):
                try:
                    audio_bytes = cc_audio.read()
                    y, sr = librosa.load(io.BytesIO(audio_bytes), sr=None, mono=True)
                    result = predictor.predict_from_array(y, sr)
                    
                    emotion = result['dominant_emotion']
                    confidence = result['confidence']
                    action = get_routing_action(emotion)
                    
                    col_pred, col_action = st.columns([1, 1])
                    
                    with col_pred:
                        st.write("#### 📊 Analisis Suara")
                        st.metric("Emosi Terdeteksi", emotion.title(), f"{(confidence*100):.1f}% Confidence")
                        
                    with col_action:
                        st.write("#### 🚦 Keputusan Routing")
                        st.markdown(f"**Prioritas:** {action['priority']}")
                        st.markdown(f"**Diarahkan Ke:** `{action['route_to']}`")
                        
                    st.warning(f"**💡 Saran Penanganan Agen:**\n{action['handling_advice']}")
                        
                except Exception as e:
                    st.error(f"Error pada sistem simulasi: {e}")
