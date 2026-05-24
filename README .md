# 🦋 Insect Species Identifier

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://insect-species-identifier-occ4vxmx8cuqtmtik9hsbo.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.18.0-orange?logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-3.8.0-red?logo=keras&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.45.1-ff4b4b?logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

An AI-powered web application that identifies **11 insect species** from images using a deep learning model built on **MobileNetV2** architecture. Simply upload a photo and get an instant prediction with confidence score.

---

## 🌐 Live Demo

👉 **[Click here to try the app](https://insect-species-identifier-occ4vxmx8cuqtmtik9hsbo.streamlit.app/)**

---

## 🐛 Supported Insect Classes

The model can identify the following 11 insect species:

| # | Species | # | Species |
|---|---------|---|---------|
| 1 | 🐜 Ant | 7 | 🦗 Grasshopper |
| 2 | 🐝 Bee | 8 | 🐞 Ladybug |
| 3 | 🪲 Beetle | 9 | 🦟 Mosquito |
| 4 | 🦋 Butterfly | 10 | 🕷️ Spider |
| 5 | 🪁 Dragonfly | 11 | 🐝 Wasp |
| 6 | 🪰 Fly | | |

---

## ✨ Features

- 📸 Upload any **JPG, JPEG, or PNG** image
- ⚡ Instant species prediction powered by **MobileNetV2**
- 📊 Confidence score for the predicted class
- 📈 Full probability breakdown for all 11 classes
- 🎨 Animated, nature-themed UI with floating insect emojis
- 🚀 Deployed and accessible from any browser — no installation needed

---

## 🧠 Model Architecture

The classifier is built using **Transfer Learning** on top of MobileNetV2:

```
Input (150 × 150 × 3)
       ↓
MobileNetV2 (pretrained base, frozen)
       ↓
GlobalAveragePooling2D
       ↓
Dense (ReLU)
       ↓
Dropout
       ↓
Dense (Softmax) → 11 classes
```

- **Base model:** MobileNetV2 (pretrained on ImageNet)
- **Input size:** 150 × 150 pixels
- **Output:** Softmax over 11 insect classes
- **Saved format:** Keras HDF5 (`.h5`)

---

## 🗂️ Project Structure

```
Insect-Species-Identifier/
│
├── app.py                        # Streamlit web application
├── insect_classifier_model.h5    # Trained Keras model
├── class_indices.json            # Class name to index mapping
├── requirements.txt              # Python dependencies
├── runtime.txt                   # Python version for Streamlit Cloud
└── README.md                     # Project documentation
```

---

## ⚙️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Frontend | Streamlit 1.45.1 |
| Deep Learning | TensorFlow 2.18.0 + Keras 3.8.0 |
| Base Model | MobileNetV2 (ImageNet weights) |
| Image Processing | Pillow 10.4.0 |
| Numerical Computing | NumPy 1.26.4 |
| Language | Python 3.12 |
| Deployment | Streamlit Community Cloud |

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Ayushsahu9903/Insect-Species-Identifier.git
cd Insect-Species-Identifier
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501` in your browser.

---

## 📦 Dependencies

```
streamlit==1.45.1
tensorflow==2.18.0
keras==3.8.0
numpy==1.26.4
Pillow==10.4.0
h5py==3.12.1
```

---

## 📸 How to Use

1. Open the [live app](https://insect-species-identifier-rgsosdkvawvpr95bj5excp.streamlit.app/)
2. Click **"Choose an image"** and upload a photo of an insect (JPG/PNG)
3. Click **"🔍 Identify Species"**
4. View the predicted species and confidence score
5. Expand **"📊 All class probabilities"** to see full results

---

## 👨‍💻 Author

**Ayush Sahu**

[![GitHub](https://img.shields.io/badge/GitHub-Ayushsahu9903-black?logo=github)](https://github.com/Ayushsahu9903)

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

<p align="center">Made with ❤️ and 🦋 by Ayush Sahu</p>
