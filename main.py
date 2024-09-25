import streamlit as st
import requests

# Title of the web app
st.title("Simple Web Form")

# Text input fields
note = st.text_area("Enter your name")

# Button to submit the form
if st.button("Submit"):
    # Create a dictionary of form data
    data = {
        "note": note
    }

    # Make a POST request to your API
    response = requests.post("https://p0dzsuv201.execute-api.us-east-2.amazonaws.com/prod/SOAPToDx", json=data)

    # Check the response
    if response.status_code == 200:
        codes = response.json()["codes"]
        explanation = response.json()["response"]
        st.success(f"Response: {codes}\n\n\nExplanation: {explanation}")

    else:
        st.error(f"Failed to fetch response. Status code: {response.status_code}")