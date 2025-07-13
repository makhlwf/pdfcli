
import unittest
import os
from PyPDF2 import PdfReader
from pdfcli.merge import merge_pdfs

class TestMerge(unittest.TestCase):

    def setUp(self):
        # Create dummy PDF files for testing
        self.pdf1_path = 'test1.pdf'
        self.pdf2_path = 'test2.pdf'
        self.output_path = 'output.pdf'

        # Create dummy PDF content
        from PyPDF2 import PdfWriter

        writer1 = PdfWriter()
        writer1.add_blank_page(width=100, height=100)
        with open(self.pdf1_path, 'wb') as f:
            writer1.write(f)

        writer2 = PdfWriter()
        writer2.add_blank_page(width=100, height=100)
        with open(self.pdf2_path, 'wb') as f:
            writer2.write(f)

    def tearDown(self):
        # Clean up dummy files
        if os.path.exists(self.pdf1_path):
            os.remove(self.pdf1_path)
        if os.path.exists(self.pdf2_path):
            os.remove(self.pdf2_path)
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_merge_pdfs(self):
        merge_pdfs([self.pdf1_path, self.pdf2_path], self.output_path)
        self.assertTrue(os.path.exists(self.output_path))
        with open(self.output_path, 'rb') as f:
            reader = PdfReader(f)
            self.assertEqual(len(reader.pages), 2)

if __name__ == '__main__':
    unittest.main()
