from unittest.mock import MagicMock, patch

import pytest
import streamlit as st

from libs.Interface.Interface import main


def test_main():
    main()
    assert True


def test_main_resume_processing(
    mock_setup_logging,
    mock_logger,
    mock_file_uploader,
    mock_subprocess_run,
    mock_selectbox,
    mock_tabs,
    mock_button,
    mock_extract_data,
):

    mock_file_uploader.return_value = "dummy_file"
    mock_subprocess_run.return_value.stdout = "model1\nmodel2\n"
    mock_selectbox.return_value = "model1"
    mock_tabs[0].write("Processed Resume Test")
    mock_button.side_effect = [True, False]
    mock_extract_data.return_value = "Processed Resume"

    main()

    mock_setup_logging.assert_called_once()
    mock_logger.info.assert_any_call("Starting the application")
    mock_extract_data.assert_called_once_with(uploaded_file="dummy_file", model_name="model1")
    mock_logger.info.assert_any_call("Resume processed successfully")


def test_main_job_fit_processing(
    mock_setup_logging,
    mock_logger,
    mock_file_uploader,
    mock_subprocess_run,
    mock_selectbox,
    mock_tabs,
    mock_button,
    mock_text_area,
    mock_job_fit,
):

    mock_file_uploader.return_value = "dummy_file"
    mock_subprocess_run.return_value.stdout = "model1\nmodel2\n"
    mock_selectbox.return_value = "model1"
    mock_tabs[1].write("Job Fit Analysis Test")
    mock_button.side_effect = [False, True]
    mock_text_area.return_value = "dummy job description"
    mock_job_fit.return_value = "Job Fit Analysis"

    main()

    mock_setup_logging.assert_called_once()
    mock_logger.info.assert_any_call("Starting the application")
    mock_job_fit.assert_called_once_with(
        uploaded_file="dummy_file", model_name="model1", job_description="dummy job description"
    )
    mock_logger.info.assert_any_call("Job fit analysis completed")
