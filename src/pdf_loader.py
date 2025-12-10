import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_pdf):
    text = ""
    pdf = fitz.open(stream=uploaded_pdf.read(), filetype="pdf")
    for page in pdf:
        text += page.get_text()
    return text
