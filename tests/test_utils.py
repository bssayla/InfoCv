import pytest
from InfoCV.utils.extraction import *

def test_extract_text_from_pdf():
    pdf_path = "tests/test_files/test_pdf.pdf"
    text = extract_text_from_pdf(pdf_path)
    assert len(text) > 0