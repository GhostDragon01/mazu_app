import streamlit as st
from home_page import home_page
from azure_ml_service_page import azure_ml_page
from custom_vision_page import custom_vision_page
from docker_page import docker_page

# Main app
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select a page", ("Home", "Azure ML Service", "Custom Vision Service", "Docker"))

    if page == "Home":
        home_page()

    elif page == "Azure ML Service":
        azure_ml_page()

    elif page == "Custom Vision Service":
        custom_vision_page()

    elif page == "Docker":
        docker_page()

if __name__ == "__main__":
    main()
