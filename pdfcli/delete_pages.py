
from PyPDF2 import PdfReader, PdfWriter

def delete_pages(input_path, output_path, pages_to_delete):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    # Convert page numbers to 0-based index and sort in descending order
    # to avoid issues when deleting pages
    pages_to_delete_set = set(int(p) - 1 for p in pages_to_delete.split(','))

    for i, page in enumerate(reader.pages):
        if i not in pages_to_delete_set:
            writer.add_page(page)

    with open(output_path, 'wb') as f:
        writer.write(f)
