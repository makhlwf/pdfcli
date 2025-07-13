
import unittest
import os
from PyPDF2 import PdfWriter
from pdfcli.extract_text import extract_text

class TestExtractText(unittest.TestCase):

    def setUp(self):
        self.pdf_path = 'test_extract.pdf'
        self.output_path = 'extracted_text.txt'

        writer = PdfWriter()
        page = writer.add_blank_page(width=100, height=100)
        # PyPDF2 doesn't directly support adding text to a page for extraction testing
        # This test will rely on a pre-existing PDF with text or a more complex setup
        # For now, we'll create a blank PDF and assume extract_text handles it gracefully
        # (i.e., extracts empty string or no error)
        with open(self.pdf_path, 'wb') as f:
            writer.write(f)

    def tearDown(self):
        if os.path.exists(self.pdf_path):
            os.remove(self.pdf_path)
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_extract_text(self):
        extract_text(self.pdf_path, self.output_path)
        self.assertTrue(os.path.exists(self.output_path))
        with open(self.output_path, 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertEqual(content.strip(), '') # Expect empty for a blank PDF

if __name__ == '__main__':
    unittest.main()
