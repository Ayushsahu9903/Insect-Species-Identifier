import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import json

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Insect Explorer",
    page_icon="🦋",
    layout="centered"
)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    try:
        model = tf.keras.models.load_model("insect_classifier_model.h5")
        return model
    except Exception:
        st.error("❌ Failed to load the AI model.")
        st.stop()

model = load_model()

# ---------------- LOAD CLASS LABELS ----------------
with open("class_indices.json", "r") as f:
    class_indices = json.load(f)

CLASS_NAMES = list(class_indices.keys())

# ---------------- CUSTOM CSS ----------------
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

        .title {
            font-size: 36px;
            color: green;
            font-weight: bold;
            text-align: center;
        }

        .sub-title {
            font-size: 30px;
            color: #0d47a1;
            font-weight: bold;
            text-align: center;
        }

        .emoji-float {
            position: fixed;
            font-size: 30px;
            opacity: 0.85;
            z-index: 0;
            pointer-events: none;
        }

        @keyframes fly {
            0% {
                transform: translateY(100vh) rotate(0deg);
            }
            100% {
                transform: translateY(-120vh) rotate(360deg);
            }
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

# ---------------- FLOATING EMOJIS ----------------
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

# ---------------- TITLE ----------------
st.markdown(
    '<div class="title">🦋 Insect Explorer</div>',
    unsafe_allow_html=True
)

st.write("Upload an image to identify the insect species.")

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    if st.button("🔍 Identify Species"):

        with st.spinner("Identifying..."):

            # Resize image
            image = image.resize((150, 150))

            # Convert to array
            img_array = np.array(image) / 255.0

            # Expand dimensions
            img_array = np.expand_dims(img_array, axis=0)

            # Predict
            prediction = model.predict(img_array)

            predicted_index = np.argmax(prediction)

            predicted_class = CLASS_NAMES[predicted_index]

            confidence = float(np.max(prediction)) * 100

            # Result
            st.markdown(
                f'<div class="sub-title">Result: 🐞 {predicted_class}</div>',
                unsafe_allow_html=True
            )

            st.success(f"Confidence: {confidence:.2f}%")

else:
    st.info("Please upload an image.")
