
from setuptools import setup, find_packages

setup(
    name='pdfcli',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'PyPDF2',
        'reportlab',
        'Pillow',
        'PyMuPDF',
    ],
    entry_points={
        'console_scripts': [
            'pdfcli = pdfcli.main:main',
        ],
    },
)
