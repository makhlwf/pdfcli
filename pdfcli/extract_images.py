
import fitz  # PyMuPDF

def extract_images(input_path, output_folder):
    doc = fitz.open(input_path)
    for i in range(len(doc)):
        for img in doc.get_page_images(i):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            with open(f"{output_folder}/image_{i+1}_{xref}.{image_ext}", "wb") as f:
                f.write(image_bytes)
    doc.close()
