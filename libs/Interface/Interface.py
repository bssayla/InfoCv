import logging
import os

import streamlit as st
from dotenv import load_dotenv
from huggingface_hub import login
from transformers import AutoModelForCausalLM, AutoTokenizer

from libs.models.API import process_resume
from libs.utils.extraction import extract_text_from_docx, extract_text_from_pdf
from libs.utils.logging_config import setup_logging


def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    load_dotenv()
    TOKEN = os.getenv("HF_TOKEN")
    if not TOKEN:
        logger.error("Hugging Face token not found in environment variables")
        return
    login(token=TOKEN, add_to_git_credential=True)
    logger.info("Logged into Hugging Face Hub")

    # get a file from the user
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx"])
    model_name = st.selectbox(
        "Choose a model", ["google/gemma-7b", "meta-llama/Meta-Llama-3.1-8B-Instruct"]
    )
    button = st.button("Process Resume")

    if uploaded_file and button:
        logger.info(f"Processing file: {uploaded_file.name} with model: {model_name}")
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        file_extension = uploaded_file.name.split(".")[-1]
        if file_extension == "pdf":
            resume_text = extract_text_from_pdf(uploaded_file)
            logger.info(f"Extracted text from PDF: {uploaded_file}")
            logger.info(f"Text: {resume_text}")
        elif file_extension == "docx":
            resume_text = extract_text_from_docx(uploaded_file)
            logger.info(f"Extracted text from DOCX: {uploaded_file}")
            logger.info(f"Text: {resume_text}")
        else:
            st.error("Invalid file type. Please upload a PDF or DOCX file.")
            logger.error("Invalid file type uploaded")
            return
        structured_resume = process_resume(resume_text, model, tokenizer)
        st.write(structured_resume)
        logger.info("Resume processed successfully")
