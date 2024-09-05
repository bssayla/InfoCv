import logging

from docx import Document
from pypdf import PdfReader


def extract_text_from_pdf(pdf_path: str) -> str:

    reader = PdfReader(pdf_path)

    file_len = len(reader.pages)
    if file_len > 2:
        raise ValueError("Le CV doit contenir au maximum 2 pages")

    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


def extract_text_from_docx(docx_path: str) -> str:

    doc = Document(docx_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text
    return text


def extract_text(uploaded_file):
    logger = logging.getLogger(__name__)
    logger.info(f"Processing file: {uploaded_file.name}")
    file_extension = uploaded_file.name.split(".")[-1]
    if file_extension == "pdf":
        resume_text = extract_text_from_pdf(uploaded_file)
        logger.info(f"Extracted text from PDF: {uploaded_file}")
        logger.info(f"Text: {resume_text}")
    elif file_extension == "docx":
        resume_text = extract_text_from_docx(uploaded_file)
        logger.info(f"Extracted text from DOCX: {uploaded_file}")
        logger.info(f"Text: {resume_text}")
    else:
        logger.error("Invalid file type uploaded")
        return "Invalid file type. Please upload a PDF or DOCX file."
    return resume_text
