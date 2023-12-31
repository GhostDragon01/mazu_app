import streamlit as st
import urllib.request
import json

seasons_list = ['winter', 'summer', 'monsoon', 'autumn', 'spring']
vegetables_list = ['potato', 'tomato', 'peas', 'pumkin', 'cucumber', 'pointed grourd', 'Raddish',
                   'Bitter gourd', 'onion', 'garlic', 'cabage', 'califlower', 'chilly', 'okra',
                   'brinjal', 'ginger', 'radish']
condition_list = ['fresh', 'scrap', 'avarage', 'scarp']
months_list = ["jan", "feb", "march", "apr", "may", "june", "july","aug", "sept", "oct", "nov", "dec"]


st.title("💰 Price Prediction")

st.markdown(
    """
    This page allows you to provide input data and make predictions on vegetable prices using **Azure Machine Learning service**.
    
    The model was trained using the data from the [Vegetable market Kaggle dataset](https://www.kaggle.com/datasets/sudipsamanta35/vegetable-market)
    
    The model predicts the price per kg of the vegetable based on the input data provided.

    The prediction is made using the **Azure Machine Learning service** deployed as a web service.
    """)

st.write("Enter the input data:")
vegetable = st.selectbox("Vegetable", vegetables_list)
season = st.selectbox("Season", seasons_list)
month = st.selectbox("Month", months_list)
temp = st.number_input("Temperature", value=0)
disaster = st.radio("Disaster Happened in Last 3 Months", ("Yes", "No"))
condition = st.selectbox("Vegetable Condition", condition_list)

predict_button = st.button("Predict")
if predict_button:
    data = {
        "Inputs": {
            "input1": [
                {
                    "Vegetable": vegetable,
                    "Season": season,
                    "Month": month,
                    "Temp": temp,
                    "Deasaster Happen in last 3month": disaster,
                    "Vegetable condition": condition
                }
            ]
        },
        "GlobalParameters": {}
    }

    api_key = 'vUmrMS6DAX0VlGlcpRxqDQz5CEET77lw'  # Replace with the primary/secondary key or AMLToken for the endpoint
    if not api_key:
        st.error("A key should be provided to invoke the endpoint.")

    headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}
    body = str.encode(json.dumps(data))
    url = 'http://0e716dec-8f88-44b1-b174-a19500038284.westeurope.azurecontainer.io/score'

    try:
        req = urllib.request.Request(url, body, headers)
        response = urllib.request.urlopen(req)
        result = response.read()
        parsed_result = json.loads(result)
        price_per_kg = parsed_result["Results"]["WebServiceOutput0"][0]["Price per kg"]
        st.write("Prediction Result:")
        st.markdown(
            f"""
            Price per kg:
            - Indian Rupee (₹): **{round(float(price_per_kg), 3)}**
            - US Dollar ($): **{round(float(price_per_kg) * 0.0122, 3)}**
            - Euro (€): **{round(float(price_per_kg) * 0.0111, 3)}**
            """)
    except urllib.error.HTTPError as error:
        st.error("The request failed with status code: " + str(error.code))
        st.write(error.info())
        st.write(error.read().decode("utf8", 'ignore'))
