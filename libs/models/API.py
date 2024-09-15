import logging
from typing import Optional

from langchain_ollama import OllamaLLM

from libs.prompts.csv_prompts import (
    extract_data_from_resume_as_csv_1,
    extract_data_from_resume_as_csv_2,
    extract_data_from_resume_as_csv_3,
    extract_data_from_resume_as_csv_4,
    extract_data_from_resume_as_csv_5,
)
from libs.prompts.job_fit_prompts import job_fitting_prompt_1
from libs.prompts.json_prompts import extract_data_from_resume_as_json_1
from libs.utils.extraction import extract_text

resume_anlysis_prompt_to_try = extract_data_from_resume_as_json_1
job_fitting_prompt_to_try = job_fitting_prompt_1


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
        prompt = job_fitting_prompt_to_try.format(
            resume_text=resume_text, job_description=job_description
        )
    elif type_of_analysis == "resume_analysis":
        logger.info("Getting prompt for resume analysis")
        prompt = resume_anlysis_prompt_to_try.format(resume_text=resume_text)

    # get the model response
    model = OllamaLLM(model=model_name)
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
