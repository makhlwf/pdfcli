
import unittest
import os
from PyPDF2 import PdfReader, PdfWriter
from pdfcli.rotate import rotate_pdf

class TestRotate(unittest.TestCase):

    def setUp(self):
        self.pdf_path = 'test.pdf'
        self.output_path = 'rotated.pdf'

        writer = PdfWriter()
        writer.add_blank_page(width=100, height=200)
        with open(self.pdf_path, 'wb') as f:
            writer.write(f)

    def tearDown(self):
        if os.path.exists(self.pdf_path):
            os.remove(self.pdf_path)
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_rotate_pdf(self):
        rotate_pdf(self.pdf_path, self.output_path, 90)
        self.assertTrue(os.path.exists(self.output_path))
        with open(self.output_path, 'rb') as f:
            reader = PdfReader(f)
            page = reader.pages[0]
            self.assertEqual(page.rotation, 90)

if __name__ == '__main__':
    unittest.main()
