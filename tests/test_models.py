from unittest.mock import MagicMock, patch

import pytest

from libs.models.API import Extract_Data, Job_Fit, Ollama_Locally


@patch("libs.models.API.extract_text")
@patch("libs.models.API.OllamaLLM")
def test_Ollama_Locally_job_fit(mock_OllamaLLM, mock_extract_text):
    mock_extract_text.return_value = "Sample resume text"
    mock_model = MagicMock()
    mock_model.invoke.return_value = "Mocked model response"
    mock_OllamaLLM.return_value = mock_model

    uploaded_file = "dummy_file_path"
    model_name = "dummy_model"
    job_description = "Sample job description"
    type_of_analysis = "job_fit"

    response = Ollama_Locally(uploaded_file, model_name, type_of_analysis, job_description)

    mock_extract_text.assert_called_once_with(uploaded_file)
    mock_OllamaLLM.assert_called_once_with(model=model_name)
    mock_model.invoke.assert_called_once()
    assert response == "Mocked model response"


@patch("libs.models.API.extract_text")
@patch("libs.models.API.OllamaLLM")
def test_Ollama_Locally_resume_analysis(mock_OllamaLLM, mock_extract_text):
    mock_extract_text.return_value = "Sample resume text"
    mock_model = MagicMock()
    mock_model.invoke.return_value = "Mocked model response"
    mock_OllamaLLM.return_value = mock_model

    uploaded_file = "dummy_file_path"
    model_name = "dummy_model"
    type_of_analysis = "resume_analysis"

    response = Ollama_Locally(uploaded_file, model_name, type_of_analysis)

    mock_extract_text.assert_called_once_with(uploaded_file)
    mock_OllamaLLM.assert_called_once_with(model=model_name)
    mock_model.invoke.assert_called_once()
    assert response == "Mocked model response"


@patch("libs.models.API.Ollama_Locally")
def test_Job_Fit(mock_Ollama_Locally):
    mock_Ollama_Locally.return_value = "Mocked job fit response"

    uploaded_file = "dummy_file_path"
    model_name = "dummy_model"
    job_description = "Sample job description"

    response = Job_Fit(uploaded_file, model_name, job_description)

    mock_Ollama_Locally.assert_called_once_with(
        uploaded_file, model_name, "job_fit", job_description
    )
    assert response == "Mocked job fit response"


@patch("libs.models.API.Ollama_Locally")
def test_Extract_Data(mock_Ollama_Locally):
    mock_Ollama_Locally.return_value = "Mocked resume analysis response"

    uploaded_file = "dummy_file_path"
    model_name = "dummy_model"

    response = Extract_Data(uploaded_file, model_name)

    mock_Ollama_Locally.assert_called_once_with(uploaded_file, model_name, "resume_analysis")
    assert response == "Mocked resume analysis response"
