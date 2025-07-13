
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_path, output_path_prefix, page_ranges):
    pdf_reader = PdfReader(input_path)
    for i, page_range in enumerate(page_ranges):
        pdf_writer = PdfWriter()
        start, end = map(int, page_range.split('-'))
        for page_num in range(start - 1, end):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        output_path = f'{output_path_prefix}_{i + 1}.pdf'
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)
