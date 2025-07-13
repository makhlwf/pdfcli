
import unittest
import os
from PyPDF2 import PdfWriter
from pdfcli.extract_images import extract_images

class TestExtractImages(unittest.TestCase):

    def setUp(self):
        self.pdf_path = 'test_images.pdf'
        self.output_dir = 'extracted_images'
        os.makedirs(self.output_dir, exist_ok=True)

        # Create a dummy PDF with a blank page (no images to extract, but for testing flow)
        writer = PdfWriter()
        writer.add_blank_page(width=100, height=100)
        with open(self.pdf_path, 'wb') as f:
            writer.write(f)

    def tearDown(self):
        if os.path.exists(self.pdf_path):
            os.remove(self.pdf_path)
        if os.path.exists(self.output_dir):
            for f in os.listdir(self.output_dir):
                os.remove(os.path.join(self.output_dir, f))
            os.rmdir(self.output_dir)

    def test_extract_images(self):
        extract_images(self.pdf_path, self.output_dir)
        # For a blank PDF, no images should be extracted
        self.assertEqual(len(os.listdir(self.output_dir)), 0)

if __name__ == '__main__':
    unittest.main()
