import logging

import pytest

from libs.utils.extraction import extract_text, extract_text_from_docx, extract_text_from_pdf
from libs.utils.logging_config import setup_logging
from unittest.mock import MagicMock, patch


def test_extract_text_from_pdf():
    pdf_path = "data/data_raw/PDF/1.pdf"
    text = extract_text_from_pdf(pdf_path)
    assert len(text) > 0


def test_extract_text_from_docx():
    docx_path = "data/data_raw/Docx/1.docx"
    text = extract_text_from_docx(docx_path)
    assert len(text) > 0


def test_setup_logging():
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Test logging")
    assert True


def test_extract_text():
    mock_uploaded_file = MagicMock()
    mock_uploaded_file.name = "1.pdf"
    with patch("libs.utils.extraction.extract_text_from_pdf") as mock_extract_text_from_pdf:
        mock_extract_text_from_pdf.return_value = "dummy text"
        text = extract_text(mock_uploaded_file)
        assert text == "dummy text"

    mock_uploaded_file.name = "1.docx"
    with patch("libs.utils.extraction.extract_text_from_docx") as mock_extract_text_from_docx:
        mock_extract_text_from_docx.return_value = "dummy text"
        text = extract_text(mock_uploaded_file)
        assert text == "dummy text"
    
    mock_extract_text_from_docx.assert_called_once_with(mock_uploaded_file)
    mock_extract_text_from_pdf.assert_called_once_with(mock_uploaded_file)
