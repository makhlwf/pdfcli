
import unittest
import os
from PIL import Image
from pdfcli.fromimages import from_images
from PyPDF2 import PdfReader

class TestFromImages(unittest.TestCase):

    def setUp(self):
        self.image1_path = 'test1.png'
        self.image2_path = 'test2.png'
        self.output_path = 'images_output.pdf'

        # Create dummy image files
        img1 = Image.new('RGB', (100, 100), color = 'red')
        img1.save(self.image1_path)

        img2 = Image.new('RGB', (100, 100), color = 'blue')
        img2.save(self.image2_path)

    def tearDown(self):
        if os.path.exists(self.image1_path):
            os.remove(self.image1_path)
        if os.path.exists(self.image2_path):
            os.remove(self.image2_path)
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_from_images(self):
        from_images([self.image1_path, self.image2_path], self.output_path)
        self.assertTrue(os.path.exists(self.output_path))
        with open(self.output_path, 'rb') as f:
            reader = PdfReader(f)
            self.assertEqual(len(reader.pages), 2)

if __name__ == '__main__':
    unittest.main()
