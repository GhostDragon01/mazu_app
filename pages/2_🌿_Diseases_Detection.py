import streamlit as st
import pandas as pd
import requests
import io
from PIL import Image

# Azure Custom Vision endpoint information
ENDPOINT_URL = "https://mazuproject2023cv-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/e3c4ed53-3a0b-4544-b101-2a186aeaa6bd/classify/iterations/Iteration2"

# Azure Custom Vision Prediction Key
PREDICTION_KEY = "314f3cd135f2435eac5e5011897c4669"


def predict_image(image):
    # Prepare the image data for the request
    image_data = io.BytesIO()
    image.save(image_data, format="JPEG")
    image_data.seek(0)

    # Send the prediction request to the Azure Custom Vision endpoint
    headers = {
        "Prediction-Key": PREDICTION_KEY,
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

def load_image_from_url(image_url):
    try:
        response = requests.get(image_url)
        image = Image.open(io.BytesIO(response.content))
        return image
    except Exception as e:
        st.write("Error loading image from URL:", str(e))


# Page title
st.title("🌿 Diseases Detection")
st.markdown(
    """
    This page allows you to upload an image or enter an image URL for prediction using **Azure Custom Vision service**.

    The model used for prediction is trained using the images from the [PlantVillage Dataset](https://www.kaggle.com/emmarex/plantdisease).
    
    The model is trained to detect the following diseases:
    - Bell Pepper Bacterial Spot
    - Bell Pepper Healthy
    - Potato Early Blight
    - Potato Late Blight
    - Potato Healthy
    - Tomato Bacterial Spot
    - Tomato Early Blight
    - Tomato Late Blight
    - Tomato Leaf Mold
    - Tomato Septoria Leaf Spot
    - Tomato Spider Mites
    - Tomato Target Spot
    - Tomato Yellow Leaf Curl Virus
    - Tomato Mosaic Virus
    - Tomato Healthy
    """)

# Image source selection
image_source = st.radio("Select Image Source", ("Local Image", "Image URL"))

# Image upload or URL input based on selection
if image_source == "Local Image":
    image_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
    if image_file is not None:
        image = Image.open(image_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        predict_button = st.button("Predict")
        if predict_button:
            predict_image(image)

elif image_source == "Image URL":
    image_url = st.text_input("Enter Image URL")
    if image_url:
        image = load_image_from_url(image_url)
        if image is not None:
            st.image(image, caption="Image from URL", use_column_width=True)
            predict_button = st.button("Predict")
            if predict_button:
                predict_image(image)


