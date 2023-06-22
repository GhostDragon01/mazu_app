import streamlit as st

# Set page title and icon
st.set_page_config(page_title="PlantAI Project", page_icon="🌱")

# Page title and description
st.title("🌿 PlantAI Project")
st.write("Welcome to the PlantAI project! 🌿🔬🚀")
st.write("This project aims to utilize machine learning and computer vision techniques to assist in plant-related tasks. It provides various functionalities to predict vegetable prices, detect plant diseases, and explore Docker services for offline use.")

# Project Description
st.header("📖 Project Description")
st.write("The PlantAI project leverages Azure's machine learning and custom vision services to analyze and predict vegetable prices and detect plant diseases. Additionally, the custom vision model is exported to a Docker container for offline use. The project is built as a Streamlit application with the following pages:")

# Page Description
st.header("📚 Pages Overview")

# Home Page
st.subheader("🏠 Home")
st.write("The Home page provides an overview of the project, its purpose, and the functionalities offered by each page.")

# Price Prediction Page
st.subheader("💰 Price Prediction")
st.write("The Price Prediction page allows you to input various factors such as vegetable type, season, month, temperature, disasters in the last 3 months, and vegetable condition. Based on these inputs, the page utilizes Azure's machine learning service to predict the price per kilogram for the selected vegetable.")

# Diseases Detection Page
st.subheader("🌿 Diseases Detection")
st.write("The Diseases Detection page enables you to upload an image or provide an image URL of a plant leaf. It utilizes Azure's custom vision service to analyze the image and detect potential diseases or conditions affecting the plant. The results are displayed, providing insights into the identified diseases and their probabilities.")

# Docker Service Page
st.subheader("🐳 Docker Service")
st.write("The Docker Service page demonstrates the offline usage of the custom vision model. It allows you to upload a local image and utilizes a Docker container to perform the same disease detection as the online Custom Vision service. The results are displayed, showcasing the model's capability even without an internet connection.")

# Project Conclusion
st.header("🚀 Conclusion")
st.write("The PlantAI project harnesses the power of machine learning and computer vision to assist in vegetable price prediction and plant disease detection. With the user-friendly Streamlit interface, users can easily access and utilize the project's functionalities. Explore the different pages to experience the benefits of PlantAI!")

# Authors
st.header("👥 Authors")

st.markdown(
    """
    - **Habib ADOUM MANDAZOU**
    - **Noé BONNE**
    - **Reyane EN-NABTY**
    - **Mathieu LATOURNERIE**
    - **Armand MOUNSI**
    """)