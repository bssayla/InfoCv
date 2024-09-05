import logging

import pytest

from libs.utils.extraction import extract_text_from_docx, extract_text_from_pdf, extract_text
from libs.utils.logging_config import setup_logging


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
   pass