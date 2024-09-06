import logging
from typing import Optional

from langchain_ollama import OllamaLLM
from transformers import AutoModelForCausalLM, AutoTokenizer

from libs.prompts.prompt import get_prompt
from libs.utils.extraction import extract_text

PROMPT_NUM = 6


def process_resume(resume_text, model_name: str):
    logger = logging.getLogger(__name__)
    prompt = get_prompt(PROMPT_NUM, resume_text)
    response = Ollama_Locally(prompt, model_name)
    logger.info("Resume processing completed")
    return response


def Ollama_Locally(
    uploaded_file, model_name: str, type_of_analysis: str, job_description: Optional[str] = None
) -> str:

    logger = logging.getLogger(__name__)
    logger.info("Ollama Locally started")
    response = "The model is not implemented yet"

    resume_text = extract_text(uploaded_file)
    # get the prompt
    if type_of_analysis == "job_fit":
        logger.info("Getting prompt for job fit analysis")
        prompt = get_prompt(5, resume_text, job_description)
    elif type_of_analysis == "resume_analysis":
        logger.info("Getting prompt for resume analysis")
        prompt = get_prompt(PROMPT_NUM, resume_text)

    # get the model response
    if model_name == "meta-llama/Meta-Llama-3.1-8B-Instruct":
        model = OllamaLLM(model="llama3.1:8b")
        response = model.invoke(input=prompt)
    elif model_name == "google/gemma-2-9b":
        model = OllamaLLM(model="llama3.1:8b")
        response = model.invoke(input=prompt)
    logger.info("Model response received")
    return response


def Job_Fit(uploaded_file, model_name, job_description):
    logger = logging.getLogger(__name__)
    logger.info("Starting job fit analysis")

    model_response = Ollama_Locally(uploaded_file, model_name, "job_fit", job_description)
    return model_response


def Extract_Data(uploaded_file, model_name):
    logger = logging.getLogger(__name__)
    logger.info("Starting resume processing")
    model_response = Ollama_Locally(uploaded_file, model_name, "resume_analysis")
    return model_response
