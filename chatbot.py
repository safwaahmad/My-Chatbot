import streamlit as st
from langchain.llms import HuggingFaceHub
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the Hugging Face API token from environment variables
hf_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')

if hf_token is None:
    st.error("HUGGINGFACEHUB_API_TOKEN environment variable is not set.")
else:
    # Initialize the HuggingFace model
    repo_id = "gpt2"  # Make sure this is the correct repository ID
    llm = HuggingFaceHub(
        repo_id=repo_id,
        huggingfacehub_api_token=hf_token,
        model_kwargs={"max_length": 128, "temperature": 0.7}
    )

    # Streamlit interface
    st.title("Chat with GPT-2")
    st.write("This chatbot is powered by a GPT-2 model hosted on Hugging Face.")

    user_input = st.text_input("You:", "Type your message here...")

    if st.button("Send"):
        if user_input:
            try:
                response = llm(user_input)
                st.write(f"Bot: {response}")
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.write("Please enter a message.")
