
from PyPDF2 import PdfReader, PdfWriter

def rotate_pdf(input_path, output_path, rotation):
    pdf_reader = PdfReader(input_path)
    pdf_writer = PdfWriter()

    for page in pdf_reader.pages:
        page.rotate(rotation)
        pdf_writer.add_page(page)

    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)
