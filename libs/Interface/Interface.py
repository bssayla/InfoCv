import logging
import os

import streamlit as st
from dotenv import load_dotenv
from huggingface_hub import login

from libs.models.API import HuggingFace_API, Ollama_Locally
from libs.utils.logging_config import setup_logging


def main():
    structured_resume = "Error: Something went wrong"
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Starting the application")
    # get a file from the user
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx"])
    model_name = st.selectbox(
        "Choose a model", ["google/gemma-2-9b", "meta-llama/Meta-Llama-3.1-8B-Instruct"]
    )
    type_of_analysis = st.radio(
        "Choose the type of analysis", ["Ollama Locally", "HuggingFace API"], index=0
    )
    button = st.button("Process Resume")

    if uploaded_file and button:
        if type_of_analysis == "HuggingFace API":
            load_dotenv()
            TOKEN = os.getenv("HF_TOKEN")
            if not TOKEN:
                logger.error("Hugging Face token not found in environment variables")
                return
            login(token=TOKEN, add_to_git_credential=True)
            logger.info("Logged into Hugging Face Hub successfully")
            structured_resume = HuggingFace_API(uploaded_file, model_name)
        elif type_of_analysis == "Ollama Locally":
            logger.info("Starting Ollama Locally")
            structured_resume = Ollama_Locally(uploaded_file, model_name)
        st.write(structured_resume)
        logger.info("Resume processed successfully")
