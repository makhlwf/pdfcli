from PyPDF2 import PdfReader

def extract_text(input_path, output_path):
    reader = PdfReader(input_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
