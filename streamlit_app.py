import streamlit as st
import numpy as np
import pickle
import os
import base64
from PIL import Image
import streamlit.components.v1 as components

# Fungsi encode background
def set_bg_from_local(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    return encoded_string

# Encode background dari folder assets
encoded_string = set_bg_from_local("assets/background_UI-ml1.png")

# Inject CSS
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Orbitron', sans-serif;
    }}
    h1, h2, h3 {{
        color: #00FFC6;
        text-shadow: 0 0 10px #00FFC6;
    }}
    .stButton>button {{
        background-color: #00FFC6;
        color: #0C3B5D;
        font-weight: bold;
        border-radius: 10px;
        box-shadow: 0 0 15px #00FFC6;
    }}
    .stButton>button:hover {{
        background-color: #00CCAA;
    }}
    .stNumberInput>div>input {{
        background-color: #122C44;
        color: #00FFC6;
        border-radius: 10px;
    }}
    img {{
        border: 2px solid #00FFC6;
        border-radius: 12px;
        box-shadow: 0 0 15px #00FFC6;
    }}
    footer {{visibility: hidden;}}
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# Radar SVG Animation
radar_html = """
<style>
.radar-wrapper {
    position: relative;
    width: 200px;
    height: 200px;
    margin: auto;
    margin-bottom: 30px;
}
.radar {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: radial-gradient(circle, #00ffc620 2%, transparent 60%);
    border: 2px solid #00FFC6;
    position: relative;
    box-shadow: 0 0 15px #00FFC6;
    overflow: hidden;
}
.radar::before {
    content: "";
    position: absolute;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: linear-gradient(90deg, #00FFC6 0%, transparent 70%);
    transform-origin: center;
    animation: rotate 2s linear infinite;
    opacity: 0.6;
}
@keyframes rotate {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
</style>
<div class="radar-wrapper">
    <div class="radar"></div>
</div>
"""

# Load model
MODEL_PATH = "models/linear_model.pkl"
if not os.path.exists(MODEL_PATH):
    st.error("❗ Model belum tersedia. Jalankan `main.py` terlebih dahulu.")
    st.stop()

with open(MODEL_PATH, "rb") as file:
    loaded_model = pickle.load(file)

# === UI Streamlit ===
st.title("Linear Regression - AI Prediction")
st.markdown("#### Powered by Linear Regression")
components.html(radar_html, height=250)

col1, col2 = st.columns([1, 2])
with col1:
    st.markdown("### Input Data")
    x_input = st.number_input("Masukkan nilai X", value=0.0, step=0.1, format="%.2f")
    if st.button("🔍 Prediksi"):
        x_array = np.array([[x_input]])
        y_output = loaded_model.predict(x_array)
        st.success(f"📈 Prediksi Y: **{y_output[0][0]:.2f}**")

with col2:
    st.markdown("### Model Insight")
    st.markdown("- Model: **Linear Regression**")
    st.markdown("- Interaktif, ringan, dan cepat")
    st.markdown("- Dataset dummy dengan noise")
    st.markdown("- Digunakan untuk simulasi prediksi real-time")

# Tabs Tambahan
st.markdown("---")
st.markdown("###  Modul")
tab1, tab2 = st.tabs(["📊 Visualisasi", "📄 Penjelasan"])

with tab1:
    if os.path.exists("regression_plot.png"):
        st.image(Image.open("regression_plot.png"), caption="Grafik Regresi", use_container_width=True)
    else:
        st.warning("⚠️ Gambar 'regression_plot.png' belum tersedia.")

with tab2:
    st.markdown("""
    **Penjelasan Model:**

    - Dataset terdiri dari variabel `X` dan target `Y` dengan sedikit noise.
    - Model dilatih menggunakan **LinearRegression()** dari `scikit-learn`.
    - Tujuan: memprediksi nilai `Y` berdasarkan input `X`.
    - Evaluasi dan visualisasi model disimpan dalam `main.py`.

    **Framework & Library:**
    - Streamlit (UI Futuristik)
    - Pickle (Model Serialization)
    - Matplotlib (Visualisasi)
    """)

# Footer
st.markdown("""
    <hr style="border: 1px solid #00FFFF;">
    <center>
        <small>🚀 Developed with ❤️ using Streamlit | Create by arielshakaramiro</small>
    </center>
""", unsafe_allow_html=True)