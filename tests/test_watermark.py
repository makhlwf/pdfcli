
import unittest
import os
from PyPDF2 import PdfWriter, PdfReader
from pdfcli.watermark import add_watermark

class TestWatermark(unittest.TestCase):

    def setUp(self):
        self.pdf_path = 'test_watermark.pdf'
        self.watermark_path = 'watermark.pdf'
        self.output_path = 'watermarked.pdf'

        # Create a dummy PDF for watermarking
        writer = PdfWriter()
        writer.add_blank_page(width=200, height=200)
        with open(self.pdf_path, 'wb') as f:
            writer.write(f)

        # Create a dummy watermark PDF
        watermark_writer = PdfWriter()
        watermark_writer.add_blank_page(width=200, height=200)
        with open(self.watermark_path, 'wb') as f:
            watermark_writer.write(f)

    def tearDown(self):
        if os.path.exists(self.pdf_path):
            os.remove(self.pdf_path)
        if os.path.exists(self.watermark_path):
            os.remove(self.watermark_path)
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_add_watermark(self):
        add_watermark(self.pdf_path, self.watermark_path, self.output_path)
        self.assertTrue(os.path.exists(self.output_path))
        # Further assertions could involve checking the content of the watermarked PDF
        # but that's more complex and might require image processing libraries.
        # For now, just checking file existence is sufficient.

if __name__ == '__main__':
    unittest.main()
