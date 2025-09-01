import os
import joblib
import streamlit as st
import gdown
import numpy as np

# Google Drive file ID
FILE_ID = "1G1N70bS03ZLOhOmYK2wCrpT7lTXW9ZKz"
MODEL_PATH = "Hazardous_Deploy.pkl"

def load_model():
    if not os.path.exists(MODEL_PATH):
        with st.spinner("Downloading model from Google Drive..."):
            url = f"https://drive.google.com/uc?id={FILE_ID}"
            gdown.download(url, MODEL_PATH, quiet=False)
    return joblib.load(MODEL_PATH)

model = load_model()

def predictions(data):
    pred=model.predict(data)
    if pred[0] == 1:
        return 'It is Hazardous For Earth'
    else:
        return 'It is Not Hazardous For Earth'

def main():
     # title of the web app
     st.title('Hazardous NEO Prediction Web App')

     # to get input from the user
     
     absolute_magnitude = st.number_input('Absolute Magnitude : ',format="%.2f")
     estimated_diameter_max = st.number_input('Estimated Diameter Max : ',format="%.2f")
     relative_velocity = st.number_input('Relative Velocity : ',format="%.2f")
     miss_distance = st.number_input('Miss Distance : ',format="%.2f")

     # code for button
     if st.button('Predict'):
          data = np.array([[absolute_magnitude,estimated_diameter_max,relative_velocity,miss_distance]])
          result = predictions(data)
          st.success(result)

if __name__ == '__main__':
     main()