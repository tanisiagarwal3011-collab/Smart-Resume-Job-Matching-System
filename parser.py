import os
import pymupdf


def extract_pdf_text(file_path):
    """
    Extract text from a PDF file.
    """

    pdf_document = pymupdf.open(file_path)

    text = ""

    for page in pdf_document:
        text += page.get_text()

    pdf_document.close()

    return text


