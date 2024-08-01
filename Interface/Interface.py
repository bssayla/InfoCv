import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
from utils.extraction import extract_text_from_pdf, extract_text_from_docx
from models.API import process_resume

def main():
    # get a file from the user
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx"])
    model_name = st.selectbox("Choose a model", ["meta-llama/Llama-2-7b-chat-hf", "google/gemma-7b"])
    button = st.button("Process Resume")

    if uploaded_file and button:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        file_extension = uploaded_file.name.split(".")[-1]
        if file_extension == "pdf":
            resume_text = extract_text_from_pdf(uploaded_file)
        elif file_extension == "docx":
            resume_text = extract_text_from_docx(uploaded_file)
        else:
            st.error("Invalid file type. Please upload a PDF or DOCX file.")
            return
        structured_resume = process_resume(resume_text, model, tokenizer)
        st.write(structured_resume)
        

