import streamlit as st
import cv2
import numpy as np
import tensorflow as tf
from PIL import Image
import tempfile

# Load the trained model (ensure you provide the correct path)
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("chest_xray_model.h5")  # Update with your model path

model = load_model()

# Define labels
labels = ['Atelectasis', 'Cardiomegaly', 'Consolidation', 'Edema', 'Effusion', 'Emphysema',
          'Fibrosis', 'Hernia', 'Infiltration', 'Mass', 'No Finding', 'Nodule',
          'Pleural_Thickening', 'Pneumonia', 'Pneumothorax']

def preprocess_image(image):
    """Preprocess the uploaded image."""
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # Convert RGB to BGR (OpenCV format)
    img = cv2.resize(img, (299, 299))  # Resize to model input size
    img = img.astype(np.float32) / 255.0  # Normalize
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

def classify_xray(image):
    """Classify an X-ray image and return predictions."""
    img = preprocess_image(image)
    prediction = model.predict(img)[0]  # Get predictions
    confidences = {labels[i]: float(prediction[i]) for i in range(len(labels))}
    return {label: conf for label, conf in sorted(confidences.items(), key=lambda x: x[1], reverse=True)}

# Streamlit UI
st.title("Chest X-ray Disease Classification")
st.write("Upload a chest X-ray image to classify possible diseases.")

uploaded_file = st.file_uploader("Choose an X-ray image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded X-ray Image", use_column_width=True)
    
    # Process and classify image
    predictions = classify_xray(image)
    
    # Display results
    st.subheader("Prediction Results")
    for disease, confidence in predictions.items():
        st.write(f"{disease}: {confidence:.4f}")
        st.progress(confidence)
