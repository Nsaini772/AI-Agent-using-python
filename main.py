# Note: Replace **<YOUR_APPLICATION_TOKEN>** with your actual Application token

import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

# uncomment this section

# BASE_API_URL = "https://api.langflow.astra.datastax.com"
# LANGFLOW_ID = "c61f4504-45d2-4281-893c-9e91e8ff9fb6"
# FLOW_ID = "11b0602a-2601-4c9c-a7f5-0b79c1fd83af"
# APPLICATION_TOKEN = os.environ.get("APP_TOKEN")
# ENDPOINT = "customer" # The endpoint name of the flow


def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    
    
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()


def main():
    st.title("Chat Interface")

    message = st.text_area("Message",placeholder="Ask anything...")
    if st.button("Run Flow"):
        if not message.strip():
            st.error("PLease enter a message")
            return
        
        try:
            with st.spinner("Running Flow..."):
                response = run_flow(message)
            
            response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response)
        
        except Exception as e:
            st.error(str(e))


if __name__ == "__main__":
    main()