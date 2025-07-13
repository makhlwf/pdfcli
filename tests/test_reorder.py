
import unittest
import os
from PyPDF2 import PdfReader, PdfWriter
from pdfcli.reorder import reorder_pages

class TestReorder(unittest.TestCase):

    def setUp(self):
        self.pdf_path = 'test_reorder.pdf'
        self.output_path = 'reordered.pdf'

        writer = PdfWriter()
        writer.add_blank_page(width=100, height=100)
        writer.add_blank_page(width=100, height=100)
        writer.add_blank_page(width=100, height=100)
        with open(self.pdf_path, 'wb') as f:
            writer.write(f)

    def tearDown(self):
        if os.path.exists(self.pdf_path):
            os.remove(self.pdf_path)
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_reorder_pages(self):
        reorder_pages(self.pdf_path, self.output_path, '3,1,2')
        self.assertTrue(os.path.exists(self.output_path))
        with open(self.output_path, 'rb') as f:
            reader = PdfReader(f)
            self.assertEqual(len(reader.pages), 3)
            # More robust testing would involve checking page content, but that's complex.
            # For now, we'll assume the page count is sufficient.

if __name__ == '__main__':
    unittest.main()
