import logging

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from libs.prompts.prompt import prompts
from libs.utils.extraction import extract_text_from_docx, extract_text_from_pdf

PROMPT_NUM = 4


def get_model_response(prompt, model_name: str, max_length: int = 1024):
    logger = logging.getLogger(__name__)
    logger.info("Getting model response")
    if model_name == "google/gemma-2-9b":
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16)
        input_ids = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(input_ids, max_length=max_length)
        response = tokenizer.decode(outputs[0])
    elif model_name == "meta-llama/Meta-Llama-3.1-8B-Instruct":
        # still didn't impliment the model usage in the code (CPU specially)
        pass

    logger.info("Model response received")
    return response


def process_resume(resume_text, model_name: str):
    logger = logging.getLogger(__name__)
    logger.info("Starting resume processing")
    prompt = prompts[PROMPT_NUM].format(resume_text)
    response = get_model_response(prompt, model_name)
    logger.info("Resume processing completed")
    return response


def HuggingFace_API(uploaded_file, model_name: str) -> str:
    logger = logging.getLogger(__name__)
    logger.info("Starting Hugging Face API")
    logger.info(f"Processing file: {uploaded_file.name} with model: {model_name}")
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
        logger.error("Invalid file type uploaded")
        return "Invalid file type. Please upload a PDF or DOCX file."
        return
    structured_resume = process_resume(resume_text, model_name)
    return structured_resume


def Ollama_Locally(uploaded_file, model_name: str) -> str:
    import ollama
    from langchain_ollama import OllamaLLM

    logger = logging.getLogger(__name__)
    logger.info("Ollama Locally started")
    file_extension = uploaded_file.name.split(".")[-1]
    response = "The model is not implemented yet"
    if file_extension == "pdf":
        resume_text = extract_text_from_pdf(uploaded_file)
        logger.info(f"Extracted text from PDF: {uploaded_file}")
        logger.info(f"Text: {resume_text}")
    elif file_extension == "docx":
        resume_text = extract_text_from_docx(uploaded_file)
        logger.info(f"Extracted text from DOCX: {uploaded_file}")
        logger.info(f"Text: {resume_text}")
    else:
        logger.error("Invalid file type uploaded")
        return "Invalid file type. Please upload a PDF or DOCX file."
    if model_name == "meta-llama/Meta-Llama-3.1-8B-Instruct":
        model = OllamaLLM(model="llama3.1:8b")
        prompt = prompts[PROMPT_NUM].format(resume_text)
        response = model.invoke(input=prompt)
    elif model_name == "google/gemma-2-9b":
        model = OllamaLLM(model="llama3.1:8b")
        prompt = prompts[PROMPT_NUM].format(resume_text)
        response = model.invoke(input=prompt)
    return response
