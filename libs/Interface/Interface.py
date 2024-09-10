import logging

import streamlit as st

from libs.models.API import Extract_Data, Job_Fit
from libs.utils.logging_config import setup_logging
import subprocess


def main():
    structured_resume = "Error: Something went wrong"
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Starting the application")
    # get a file from the user
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx"])
    
    # use `ollama list` command to get the list of models
    ollama_cmd_output = subprocess.run(["ollama", "list"], capture_output=True, text=True)
    ollama_cmd_output = ollama_cmd_output.stdout.split("\n")[1:-1]
    names = [name.split()[0] for name in ollama_cmd_output] or ["No models available"]
    model_name = st.selectbox(
        "Choose a model", names
    )
    resume_analysis_tab, job_fit_tab = st.tabs(["Resume Analysis", "Job Fit"])

    with resume_analysis_tab:
        button_1 = st.button("Process Resume", key="resume")

    with job_fit_tab:
        job_description = st.text_area("Enter the job description")
        button_2 = st.button("Process Job Fit", key="job_fit")

    if uploaded_file and button_1:
        structured_resume = Extract_Data(uploaded_file=uploaded_file, model_name=model_name)
        resume_analysis_tab.write(structured_resume)
        logger.info("Resume processed successfully")
    elif uploaded_file and button_2:
        structured_resume = Job_Fit(
            uploaded_file=uploaded_file, model_name=model_name, job_description=job_description
        )
        job_fit_tab.write(structured_resume)
        logger.info("Job fit analysis completed")
