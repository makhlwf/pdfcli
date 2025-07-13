
from PyPDF2 import PdfReader, PdfWriter

def protect_pdf(input_path, output_path, password):
    pdf_reader = PdfReader(input_path)
    pdf_writer = PdfWriter()

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    pdf_writer.encrypt(password)

    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)
