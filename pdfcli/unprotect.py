
from PyPDF2 import PdfReader, PdfWriter

def unprotect_pdf(input_path, output_path, password):
    pdf_reader = PdfReader(input_path)
    if pdf_reader.is_encrypted:
        pdf_reader.decrypt(password)

    pdf_writer = PdfWriter()

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)
