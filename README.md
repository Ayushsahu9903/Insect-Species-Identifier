# 🐞 Insect Species Identifier

Welcome to the **Insect Species Identifier** – an AI-powered web app that identifies insect species from images using a Convolutional Neural Network (CNN) model and a lightweight MobileNetV2 architecture.

Developed by **Pragya Srivastava**, this project blends machine learning with an interactive Streamlit interface to provide fast and accurate insect recognition.

---

## 🧠 How It Works

- ✅ Pre-trained CNN model based on **MobileNetV2**
- ✅ Input image is resized and normalized
- ✅ Model predicts the insect class from 11 categories
- ✅ Clean, user-friendly interface built with **Streamlit**

---

## 🐛 Supported Insect Classes

- Ant  
- Bee  
- Beetle  
- Butterfly  
- Dragonfly  
- Fly  
- Grasshopper  
- Ladybug  
- Mosquito  
- Spider  
- Wasp

---

## 📦 Tech Stack

- **Python**
- **TensorFlow / Keras**
- **Streamlit**
- **Pillow** (image processing)
- **NumPy**

---

## 🚀 Getting Started

### 🔧 Installation

Clone the repo:

```bash
git clone https://github.com/pragya-2765/insect-classifier-streamlit.git
cd insect-classifier-streamlit
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
▶️ Run the App
bash
Copy
Edit
streamlit run insect_identifier_app.py
Then open the provided local URL in your browser.

📁 Project Structure
bash
Copy
Edit
insect-species-identifier/
├── insect_identifier_app.py         # Main Streamlit app
├── insect_classifier_model.h5       # Trained CNN model
├── class_indices.json               # Label to class index mapping
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation

📷 Sample Image
To help you get started, we've included some example insect images in the `sample_images` folder. You can use these to test the app and see how well it performs!

👩‍💻 Authors
Pragya Srivastava

📄 License
This project is licensed under the MIT License.
