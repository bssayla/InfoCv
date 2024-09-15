import pytest


def test_internal_imports():
    from libs.evaluations import evaluate
    from libs.Interface.Interface import main
    from libs.models.API import Extract_Data, Job_Fit, Ollama_Locally
    from libs.prompts.csv_prompts import (
        extract_data_from_resume_as_csv_1,
        extract_data_from_resume_as_csv_2,
        extract_data_from_resume_as_csv_3,
        extract_data_from_resume_as_csv_4,
        extract_data_from_resume_as_csv_5,
    )
    from libs.prompts.job_fit_prompts import job_fitting_prompt_1
    from libs.prompts.json_prompts import extract_data_from_resume_as_json_1
    from libs.utils.extraction import extract_text, extract_text_from_docx, extract_text_from_pdf
    from libs.utils.logging_config import setup_logging


def test_external_imports():
    import logging
    import os
    import subprocess
    import typing

    import streamlit as st
    from docx import Document
    from dotenv import load_dotenv
    from langchain_ollama import OllamaLLM
    from pypdf import PdfReader
    from setuptools import find_packages, setup
    from transformers import AutoModelForCausalLM, AutoTokenizer
