import streamlit as st
from PIL import Image
import io, base64
import numpy as np
import os
import gdown
from ultralytics import YOLO


st.set_page_config(page_title="Ship Detection", layout="centered")

# load_model
@st.cache_resource
def load_model():
    #model = YOLO("models/best.pt")  #this file sholud be at the same folder
    #add
    model_path = "models/best.pt"
    if not os.path.exists(model_path):
        os.makedirs("models", exist_ok=True)
        url = "https://drive.google.com/drive/folders/1s23ugG10tRobWYJUVYLlQjE6lCVz4VkY"
        gdown.download(url, model_path, quit=False)
    model = YOLO(model_path)
    return model

model = load_model()

def image_to_base64(img):
    #buf = io.BytesIO
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    #buf.write(img, format="PNG")
    byte_im = buf.getvalue()
    return base64.b64encode(byte_im).decode()


st.markdown("""
    <style>
        body {
            background-color: #0c1b4d;
        }
        .main {
            background-color: #0c1b4d;
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .main-title {
            color: white;
            text-align: center;
            font-size: 4.5em !important;
            font-weight: bold;
            margin-bottom: 0.3rem !important;
            padding-top: 0.5rem;
        }
        .welcome-text {
            color: white;
            text-align: center;
            font-size: 2.2em;
            margin-bottom: 1.5rem !important;
            opacity: 0.9;
            line-height: 1.6;
        }
        .button-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 2rem;
            margin-bottom: 3rem;
            position: relative;
            padding: 0 40px;
        }
        .button-box {
            background-color: #2a3e8c;
            padding: 20px 15px;
            border-radius: 12px;
            width: 140px;
            text-align: center;
            color: white;
            font-weight: bold;
            box-shadow: 0 6px 12px rgba(0,0,0,0.3);
            font-size: 1em;
            line-height: 1.3;
            border: 1px solid #3a4e9c;
            transition: transform 0.3s ease;
        }

        .arrow {
            font-size: 3em;
            color: #3a4e9c;
            font-weight: 300;
        }
        .upload-section {
            text-align: center;
            padding: 25px;
            margin: 2rem 0;
        }
        .element-container:has(.stFileUploader) {
            max-width: 500px;
            margin-left: auto;
            margin-right: auto;
        }
        .section-title {
            color: white;
            text-align: center;
            font-size: 2.2em;
            margin: 1.5rem 0 !important;
            font-weight: bold;
        }
        .stButton button {
            background-color: #28a745 !important;
            color: white !important;
            padding: 12px 25px !important;
            border: none !important;
            border-radius: 10px !important;
            font-size: 1.1rem !important;
            font-weight: bold !important;
            margin-top: 1.5rem !important;
            width: 180px !important;
            height: 50px !important;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        .stButton button:hover {
            background-color: #218838 !important;
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.3);
        }
        .image-section {
            display: flex;
            justify-content: center;
            gap: 4rem;
            margin-top: 3rem;
            margin-bottom: 2rem;
        }
        .image-box {
            background-color: #f0f0f0;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            width: 420px;
            box-shadow: 0 6px 12px rgba(0,0,0,0.2);
        }
        .image-label {
            font-weight: bold;
            margin-bottom: 10px;
            color: #2a3e8c;
            font-size: 1.2em;
            text-align: center;
        }
        .spacer {
            height: 1rem;
        }
        .large-spacer {
            height: 2rem;
        }
        .divider {
            height: 2px;
            background: linear-gradient(90deg, transparent, #3a4e9c, transparent);
            margin: 2rem 0;
            width: 80%;
            margin-left: auto;
            margin-right: auto;
        }
        .result-text {
            text-align: center;
            font-size: 1.5em;
            color: #00ff88;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .no-result {
            text-align: center;
            font-size: 1.5em;
            color: #ff6b6b;
            font-weight: bold;
            margin-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">Ship Detection 🚢 </h1>', unsafe_allow_html=True)
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
st.markdown('<p class="welcome-text">Welcome To Ship Detection System!</p>', unsafe_allow_html=True)
st.markdown('<p class="welcome-text">Ready to detect ?</p>', unsafe_allow_html=True)

st.markdown("""
<div class="button-container">
    <div class="button-box">📤<br>Upload Image</div>
    <div class="arrow">⟶</div>
    <div class="button-box">🛠️<br>Click Detect</div>
    <div class="arrow">⟶</div>
    <div class="button-box">📊<br>Get Results</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Upload Image & Run Detection</h2>', unsafe_allow_html=True)
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'], label_visibility="collapsed")

# Detect button
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    detect = st.button("Detect Ship 🔍 ", use_container_width=True)
st.markdown('<div class="large-spacer"></div>', unsafe_allow_html=True)


if uploaded_file and detect:
    image = Image.open(uploaded_file).convert("RGB")

    with st.spinner("Detecting ships..."):
        results = model.predict(image)
        num_ships = len(results[0].boxes)

        if num_ships > 0:
            result_img = results[0].plot()
            detected_image = Image.fromarray(result_img.astype(np.uint8))
        else:
            detected_image = image

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    if num_ships > 0:
        st.markdown(f'<p class="result-text">✅ {num_ships} ship(s) detected!</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="no-result">❌ No ships detected.</p>', unsafe_allow_html=True)

    st.markdown(f"""
        <div class="image-section">
            <div class="image-wrapper">
                <div class="image-label">🖼️ ORIGINAL IMAGE</div>
                <div class="image-box">
                    <img src="data:image/png;base64,{image_to_base64(image)}" width="380"/>
                </div>
            </div>
            <div class="image-wrapper">
                <div class="image-label">🔍 DETECTION RESULT</div>
                <div class="image-box">
                    <img src="data:image/png;base64,{image_to_base64(detected_image)}" width="380"/>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
