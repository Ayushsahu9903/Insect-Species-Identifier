import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf

# Load CNN model
@st.cache_resource
def load_model():
    try:
        model = tf.keras.models.load_model("insect_classifier_model.h5")
        return model
    except Exception as e:
        st.error("❌ Failed to load the AI model.")
        st.stop()

model = load_model()

# Replace with your actual class labels
import json

with open("class_indices.json", "r") as f:
    class_indices = json.load(f)
CLASS_NAMES = list(class_indices.keys())


# App styling
st.set_page_config(page_title="Insect Explorer", layout="centered")

st.markdown("""
    <style>
        body {
            background-color: #FFFEC8;
        }
        .stApp {
            background-color: #FFFEC8;
        }
        header {
            visibility: hidden;
        }
        .title { font-size: 36px; color: green; font-weight: bold; }
        .sub-title { font-size: 30px; color: #0d47a1; font-weight: bold; }
        .upload-box {
            border: 2px dashed #4caf50;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
        }
        .result-box {
            border: 1px solid #ddd;
            padding: 15px;
            border-radius: 10px;
            background-color: #fff;
        }
        .emoji-float {
            position: fixed;
            font-size: 30px;
            opacity: 0.85;
            z-index: 0;
            pointer-events: none;
        }
        @keyframes fly {
            0% { transform: translateY(100vh) rotate(0deg); }
            100% { transform: translateY(-120vh) rotate(360deg); }
        }

        .e1 { left: 10vw; animation: fly 10s linear infinite; }
        .e2 { left: 25vw; animation: fly 12s linear infinite; }
        .e3 { left: 45vw; animation: fly 9s linear infinite; }
        .e4 { left: 65vw; animation: fly 11s linear infinite; }
        .e5 { left: 85vw; animation: fly 13s linear infinite; }
        .e6 { left: 15vw; animation: fly 14s linear infinite; }
        .e7 { left: 30vw; animation: fly 10s linear infinite; }
        .e8 { left: 55vw; animation: fly 13s linear infinite; }
        .e9 { left: 75vw; animation: fly 11s linear infinite; }

   </style>
""", unsafe_allow_html=True)


st.markdown("""
    <div class="emoji-float e1">🪰</div>
    <div class="emoji-float e2">🦋</div>
    <div class="emoji-float e3">🐝</div>
    <div class="emoji-float e4">🦗</div>
    <div class="emoji-float e5">🐞</div>
    <div class="emoji-float e6">🪲</div>
    <div class="emoji-float e7">🦟</div>
    <div class="emoji-float e8">🐛</div>
    <div class="emoji-float e9">🕷️</div>
""", unsafe_allow_html=True)



# Title
st.markdown('<div class="title">🦋 Insect Explorer</div>', unsafe_allow_html=True)
st.write("Upload an image to identify the insect species.")



# Upload image
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    if st.button("🔍 Identify Species"):
        with st.spinner("Identifying..."):
            # Preprocess image (as per your CNN input)
            image = image.resize((150, 150))  # Resize to model input shape
            img_array = np.array(image) / 255.0
            img_array = img_array.reshape(1, 150, 150, 3)

            prediction = model.predict(img_array)
            predicted_class = CLASS_NAMES[np.argmax(prediction)]
            st.markdown(f'<div class="sub-title">Result: 🐞 {predicted_class}</div>', unsafe_allow_html=True)
else:
      st.info("Please upload an image.")
