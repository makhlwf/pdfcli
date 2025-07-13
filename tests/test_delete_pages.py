
import unittest
import os
from PyPDF2 import PdfWriter, PdfReader
from pdfcli.delete_pages import delete_pages

class TestDeletePages(unittest.TestCase):

    def setUp(self):
        self.pdf_path = 'test_delete.pdf'
        self.output_path = 'deleted_pages.pdf'

        writer = PdfWriter()
        writer.add_blank_page(width=100, height=100)
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

    def test_delete_pages(self):
        delete_pages(self.pdf_path, self.output_path, '2,4')
        self.assertTrue(os.path.exists(self.output_path))
        with open(self.output_path, 'rb') as f:
            reader = PdfReader(f)
            self.assertEqual(len(reader.pages), 2) # Original 4 pages, deleted 2 and 4, so 2 remaining

if __name__ == '__main__':
    unittest.main()
