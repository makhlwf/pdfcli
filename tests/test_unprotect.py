
import unittest
import os
from PyPDF2 import PdfReader, PdfWriter
from pdfcli.protect import protect_pdf
from pdfcli.unprotect import unprotect_pdf

class TestUnprotect(unittest.TestCase):

    def setUp(self):
        self.pdf_path = 'test.pdf'
        self.protected_path = 'protected.pdf'
        self.unprotected_path = 'unprotected.pdf'
        self.password = 'testpassword'

        writer = PdfWriter()
        writer.add_blank_page(width=100, height=100)
        with open(self.pdf_path, 'wb') as f:
            writer.write(f)

        protect_pdf(self.pdf_path, self.protected_path, self.password)

    def tearDown(self):
        if os.path.exists(self.pdf_path):
            os.remove(self.pdf_path)
        if os.path.exists(self.protected_path):
            os.remove(self.protected_path)
        if os.path.exists(self.unprotected_path):
            os.remove(self.unprotected_path)

    def test_unprotect_pdf(self):
        unprotect_pdf(self.protected_path, self.unprotected_path, self.password)
        self.assertTrue(os.path.exists(self.unprotected_path))
        with open(self.unprotected_path, 'rb') as f:
            reader = PdfReader(f)
            self.assertFalse(reader.is_encrypted)

if __name__ == '__main__':
    unittest.main()
