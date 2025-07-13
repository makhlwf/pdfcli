
import unittest
import os
from PyPDF2 import PdfReader, PdfWriter
from pdfcli.protect import protect_pdf

class TestProtect(unittest.TestCase):

    def setUp(self):
        self.pdf_path = 'test.pdf'
        self.output_path = 'protected.pdf'

        writer = PdfWriter()
        writer.add_blank_page(width=100, height=100)
        with open(self.pdf_path, 'wb') as f:
            writer.write(f)

    def tearDown(self):
        if os.path.exists(self.pdf_path):
            os.remove(self.pdf_path)
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_protect_pdf(self):
        password = 'testpassword'
        protect_pdf(self.pdf_path, self.output_path, password)
        self.assertTrue(os.path.exists(self.output_path))
        with open(self.output_path, 'rb') as f:
            reader = PdfReader(f)
            self.assertTrue(reader.is_encrypted)
            self.assertIsNotNone(reader.decrypt(password))

if __name__ == '__main__':
    unittest.main()
