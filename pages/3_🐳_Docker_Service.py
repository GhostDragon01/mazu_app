import streamlit as st
import pandas as pd
import requests
import io
from PIL import Image

def predict_image(image):
    # Prepare the image data for the request
    image_data = io.BytesIO()
    image.save(image_data, format="JPEG")
    image_data.seek(0)

    # Send the prediction request to the Azure Custom Vision endpoint
    headers = {
        "Content-Type": "application/octet-stream"
    }

    response = requests.post(ENDPOINT_URL + "/image", headers=headers, data=image_data)

    # Process the prediction response
    if response.status_code == 200:
        result = response.json()
        predictions = result["predictions"]
        if predictions:
            st.write("Prediction Results:")
            table_data = [("Vegetable Name", "Probability")]
            for prediction in predictions:
                tag_name = prediction["tagName"]
                probability = prediction["probability"]
                table_data.append((tag_name, probability))
            df = pd.DataFrame(table_data[1:], columns=table_data[0])
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.write("No predictions found.")
    else:
        st.write("Prediction failed. Status code:", response.status_code)

def load_image_from_path(image_path):
    try:
        with open(image_path, "rb") as f:
            image_data = f.read()

        return image_data
    except Exception as e:
        st.write("Error loading image from the path:", str(e))


# Page title
st.title("🐳 Docker Service")
st.markdown(
    """
    This page allows you to upload an image or enter an image Path for prediction using **Docker service** for **offline use**.
    
    The model used for prediction is trained using the images from the [PlantVillage Dataset](https://www.kaggle.com/emmarex/plantdisease).
    """)

internet_status = st.radio("Internet Status", ("Online", "Offline"))

if internet_status == "Online":
    ENDPOINT_URL = "http://20.8.7.124"
    PREDICTION_KEY = "314f3cd135f2435eac5e5011897c4669"
else:
    ENDPOINT_URL = "http://localhost:8080"
    PREDICTION_KEY = "314f3cd135f2435eac5e5011897c4669"

st.write("ENDPOINT_URL:", ENDPOINT_URL)

# Image source selection
image_source = st.radio("Select Image Source", ("Local Image", "Image Path"))

# Image upload or URL input based on selection
if image_source == "Local Image":
    image_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
    if image_file is not None:
        image = Image.open(image_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        predict_button = st.button("Predict")
        if predict_button:
            predict_image(image)

elif image_source == "Image Path":
    image_path = st.text_input("Enter Image Path")
    if image_path:
        image = Image.open(image_path)
        if image is not None:
            st.image(image, caption="Image from Local Path", use_column_width=True)
            predict_button = st.button("Predict")
            if predict_button:
                predict_image(image)

