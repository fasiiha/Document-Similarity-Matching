from PyPDF2 import PdfReader

# The function reads text content from a PDF file using the PyPDF2 library.
# pdf_path: the file path to the PDF file from which we want to extract text.


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text
