from pdfminer.high_level import extract_text

def parse_resume(pdf_file):
    text = extract_text(pdf_file)
    return text
