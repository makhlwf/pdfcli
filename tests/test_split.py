
import unittest
import os
from PyPDF2 import PdfReader, PdfWriter
from pdfcli.split import split_pdf

class TestSplit(unittest.TestCase):

    def setUp(self):
        self.pdf_path = 'test.pdf'
        self.output_prefix = 'split_output'

        writer = PdfWriter()
        for _ in range(10):
            writer.add_blank_page(width=100, height=100)
        with open(self.pdf_path, 'wb') as f:
            writer.write(f)

    def tearDown(self):
        if os.path.exists(self.pdf_path):
            os.remove(self.pdf_path)
        for i in range(1, 3):
            output_path = f'{self.output_prefix}_{i}.pdf'
            if os.path.exists(output_path):
                os.remove(output_path)

    def test_split_pdf(self):
        ranges = ['1-5', '6-10']
        split_pdf(self.pdf_path, self.output_prefix, ranges)

        output1_path = f'{self.output_prefix}_1.pdf'
        output2_path = f'{self.output_prefix}_2.pdf'

        self.assertTrue(os.path.exists(output1_path))
        self.assertTrue(os.path.exists(output2_path))

        with open(output1_path, 'rb') as f:
            reader = PdfReader(f)
            self.assertEqual(len(reader.pages), 5)

        with open(output2_path, 'rb') as f:
            reader = PdfReader(f)
            self.assertEqual(len(reader.pages), 5)

if __name__ == '__main__':
    unittest.main()
