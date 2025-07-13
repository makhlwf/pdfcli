
import unittest
import os
from PyPDF2 import PdfWriter
from pdfcli.compress import compress_pdf

class TestCompress(unittest.TestCase):

    def setUp(self):
        self.pdf_path = 'test_compress.pdf'
        self.output_path = 'compressed.pdf'

        writer = PdfWriter()
        writer.add_blank_page(width=200, height=200)
        with open(self.pdf_path, 'wb') as f:
            writer.write(f)

    def tearDown(self):
        if os.path.exists(self.pdf_path):
            os.remove(self.pdf_path)
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_compress_pdf(self):
        compress_pdf(self.pdf_path, self.output_path)
        self.assertTrue(os.path.exists(self.output_path))
        # Basic check: ensure the output file is not empty
        self.assertGreater(os.path.getsize(self.output_path), 0)

if __name__ == '__main__':
    unittest.main()
