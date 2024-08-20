from pypdf import PdfReader
from docx import Document

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
