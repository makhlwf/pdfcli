
import unittest
import os
from PyPDF2 import PdfWriter
from pdfcli.to_images import to_images

class TestToImages(unittest.TestCase):

    def setUp(self):
        self.pdf_path = 'test_to_images.pdf'
        self.output_dir = 'converted_images'
        os.makedirs(self.output_dir, exist_ok=True)

        writer = PdfWriter()
        writer.add_blank_page(width=100, height=100)
        writer.add_blank_page(width=100, height=100)
        with open(self.pdf_path, 'wb') as f:
            writer.write(f)

    def tearDown(self):
        if os.path.exists(self.pdf_path):
            os.remove(self.pdf_path)
        if os.path.exists(self.output_dir):
            for f in os.listdir(self.output_dir):
                os.remove(os.path.join(self.output_dir, f))
            os.rmdir(self.output_dir)

    def test_to_images(self):
        to_images(self.pdf_path, self.output_dir)
        self.assertEqual(len(os.listdir(self.output_dir)), 2)
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, 'page_1.png')))
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, 'page_2.png')))

if __name__ == '__main__':
    unittest.main()
