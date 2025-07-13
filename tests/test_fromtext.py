
import unittest
import os
from pdfcli.fromtext import from_text
from PyPDF2 import PdfReader

class TestFromText(unittest.TestCase):

    def setUp(self):
        self.text_path = 'test.txt'
        self.output_path = 'text_output.pdf'
        with open(self.text_path, 'w') as f:
            f.write("Hello, this is a test.\n")
            f.write("This is the second line.")

    def tearDown(self):
        if os.path.exists(self.text_path):
            os.remove(self.text_path)
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_from_text_from_file(self):
        from_text(self.output_path, input_path=self.text_path)
        self.assertTrue(os.path.exists(self.output_path))
        with open(self.output_path, 'rb') as f:
            reader = PdfReader(f)
            self.assertEqual(len(reader.pages), 1)

    def test_from_text_from_raw_content(self):
        raw_content = "This is raw text content.\nAnother line of raw text."
        output_raw_path = 'raw_text_output.pdf'
        from_text(output_raw_path, text_content=raw_content)
        self.assertTrue(os.path.exists(output_raw_path))
        with open(output_raw_path, 'rb') as f:
            reader = PdfReader(f)
            self.assertEqual(len(reader.pages), 1)
        os.remove(output_raw_path)

if __name__ == '__main__':
    unittest.main()

