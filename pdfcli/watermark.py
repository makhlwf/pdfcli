
from PyPDF2 import PdfReader, PdfWriter

def add_watermark(input_path, watermark_path, output_path):
    reader = PdfReader(input_path)
    watermark_reader = PdfReader(watermark_path)
    watermark_page = watermark_reader.pages[0]

    writer = PdfWriter()
    for page in reader.pages:
        page.merge_page(watermark_page)
        writer.add_page(page)

    with open(output_path, 'wb') as f:
        writer.write(f)
