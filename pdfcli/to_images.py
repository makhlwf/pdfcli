
import fitz  # PyMuPDF

def to_images(input_path, output_folder, zoom=2):
    doc = fitz.open(input_path)
    for i, page in enumerate(doc):
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
        pix.save(f"{output_folder}/page_{i+1}.png")
    doc.close()
