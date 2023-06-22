# PlantAI Project

Welcome to the PlantAI project! 🌿🔬🚀

The PlantAI project aims to utilize machine learning and computer vision techniques to assist in plant-related tasks. It provides various functionalities to predict vegetable prices, detect plant diseases, and explore Docker services.

## Project Description

The PlantAI project leverages Azure's machine learning and custom vision services to analyze and predict vegetable prices and detect plant diseases. Additionally, the custom vision model is exported to a Docker container for offline use. The project is built as a Streamlit application with the following pages:

### Home
The Home page provides an overview of the project, its purpose, and the functionalities offered by each page.

### Price Prediction
The Price Prediction page allows you to input various factors such as vegetable type, season, month, temperature, disasters in the last 3 months, and vegetable condition. Based on these inputs, the page utilizes Azure's machine learning service to predict the price per kilogram for the selected vegetable.

### Diseases Detection
The Diseases Detection page enables you to upload an image or provide an image URL of a plant leaf. It utilizes Azure's custom vision service to analyze the image and detect potential diseases or conditions affecting the plant. The results are displayed, providing insights into the identified diseases and their probabilities.

### Docker Service
The Docker Service page demonstrates the offline usage of the custom vision model. It allows you to upload a local image and utilizes a Docker container to perform the same disease detection as the online Custom Vision service. The results are displayed, showcasing the model's capability even without an internet connection.

## Authors

The PlantAI project was developed by the following authors:
- **Habib ADOUM MANDAZOU**
- **Noé BONNE**
- **Reyane EN-NABTY**
- **Mathieu LATOURNERIE**
- **Armand MOUNSI**

## Getting Started

To get started with the PlantAI project, follow these steps:

1. Clone the repository:
`bash
git clone https://github.com/your-username/your-repository.git
`

2. Install the required dependencies:
`bash
pip install -r requirements.txt
`


3. Run the Streamlit application:
`bash
streamlit run Home.py
`


4. Access the application in your web browser at `http://localhost:8501`.

## License

This project is licensed under the [MIT License](LICENSE).
