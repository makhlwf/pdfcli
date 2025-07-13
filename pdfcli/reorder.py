
from PyPDF2 import PdfReader, PdfWriter

def reorder_pages(input_path, output_path, order):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    # Parse the order string (e.g., "1,3,2,4") into a list of integers
    page_order = [int(p) - 1 for p in order.split(',')]

    for page_num in page_order:
        writer.add_page(reader.pages[page_num])

    with open(output_path, 'wb') as f:
        writer.write(f)
