import pytest


def test_interface_imports():
    from libs.Interface.Interface import main


def test_utils_imports():
    from libs.utils.extraction import extract_text, extract_text_from_docx, extract_text_from_pdf
    from libs.utils.logging_config import setup_logging


def test_models_imports():
    from libs.models.API import Extract_Data, Job_Fit, Ollama_Locally


def test_evaluations_imports():
    import libs.evaluations.evaluate


def test_external_imports():
    import logging
    import os

    import streamlit as st
    from docx import Document
    from dotenv import load_dotenv
    from pypdf import PdfReader
    from setuptools import find_packages, setup
    from transformers import AutoModelForCausalLM, AutoTokenizer
