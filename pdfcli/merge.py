
from PyPDF2 import PdfMerger

def merge_pdfs(input_paths, output_path):
    pdf_merger = PdfMerger()
    for path in input_paths:
        pdf_merger.append(path)

    with open(output_path, 'wb') as output_file:
        pdf_merger.write(output_file)
    pdf_merger.close()
