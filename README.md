# PDF CLI

A feature-rich command-line tool for manipulating PDF files.

## Features

*   **Merge PDFs**: Combine multiple PDF files into a single document.
*   **Split PDFs**: Divide a PDF into multiple smaller files based on page ranges.
*   **Rotate Pages**: Rotate all pages in a PDF by a specified angle.
*   **Protect PDFs**: Add password protection to your PDF documents.
*   **Unprotect PDFs**: Remove password protection from PDFs.
*   **Create from Text**: Generate PDFs from text files or directly from raw text input.
*   **Create from Images**: Convert one or more image files into a PDF document.
*   **Extract Text**: Extract all text content from a PDF file.
*   **Extract Images**: Extract all images embedded within a PDF file.
*   **Convert to Images**: Convert each page of a PDF into an image file (e.g., PNG).
*   **Delete Pages**: Remove specific pages from a PDF document.
*   **Watermark PDFs**: Add a watermark (from another PDF) to your PDF documents.
*   **Reorder Pages**: Change the order of pages within a PDF.
*   **Compress PDFs**: Reduce the file size of PDF documents.

## Project Structure

```
pdfcli/
├── pdfcli/             # Main application source code
│   ├── __init__.py
│   ├── main.py         # CLI entry point
│   ├── merge.py        # PDF merging logic
│   ├── split.py        # PDF splitting logic
│   ├── rotate.py       # PDF rotation logic
│   ├── protect.py      # PDF protection logic
│   ├── unprotect.py    # PDF unprotection logic
│   ├── fromtext.py     # PDF creation from text logic
│   ├── fromimages.py   # PDF creation from images logic
│   ├── extract_text.py # Text extraction logic
│   ├── watermark.py    # Watermark adding logic
│   ├── reorder.py      # Page reordering logic
│   ├── compress.py     # PDF compression logic
│   ├── extract_images.py # Image extraction logic
│   └── to_images.py    # PDF to image conversion logic
│   └── delete_pages.py # Page deletion logic
├── tests/              # Unit tests
│   ├── __init__.py
│   ├── test_merge.py
│   ├── test_split.py
│   ├── test_rotate.py
│   ├── test_protect.py
│   ├── test_unprotect.py
│   ├── test_fromtext.py
│   ├── test_fromimages.py
│   ├── test_extract_text.py
│   ├── test_watermark.py
│   ├── test_reorder.py
│   ├── test_compress.py
│   ├── test_extract_images.py
│   ├── test_to_images.py
│   └── test_delete_pages.py
├── .github/            # GitHub Actions workflows
│   └── workflows/
│       └── main.yml
├── requirements.txt    # Python dependencies
├── setup.py            # Project setup and packaging
└── README.md           # Project documentation
```

## Installation

### Prerequisites

*   Python 3.x
*   pip (Python package installer)

### From PyPI (Coming Soon)

Once published to PyPI, you can install it directly:

```bash
pip install pdfcli
```

### From Source

1.  Clone the repository:

    ```bash
    git clone https://github.com/your-repo/pdfcli.git
    cd pdfcli
    ```

2.  Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3.  Install the package in editable mode (for development):

    ```bash
    pip install -e .
    ```

## Usage

The `pdfcli` tool uses a command-line interface. Each feature is a subcommand with its own arguments.

### General Syntax

```bash
pdfcli <command> [options]
```

### Commands

#### `merge`

Merge multiple PDF files into one.

```bash
pdfcli merge -o output.pdf input1.pdf input2.pdf [input3.pdf ...]
```

*   `-o`, `--output`: Path to the output PDF file (required).
*   `input`: Paths to the input PDF files (one or more, required).

#### `split`

Split a PDF into multiple files based on page ranges.

```bash
pdfcli split -o output_prefix -r 1-5 6-10 input.pdf
```

*   `-o`, `--output`: Output path prefix for the split files (required).
*   `-r`, `--ranges`: Page ranges to split (e.g., `1-5` for pages 1 to 5, `6-10` for pages 6 to 10).
*   `input`: Path to the input PDF file (required).

#### `rotate`

Rotate all pages in a PDF by a specified angle.

```bash
pdfcli rotate -o output.pdf -r 90 input.pdf
```

*   `-o`, `--output`: Path to the output PDF file (required).
*   `-r`, `--rotation`: Rotation angle in degrees (e.g., `90`, `180`, `270`).
*   `input`: Path to the input PDF file (required).

#### `protect`

Add a password to a PDF.

```bash
pdfcli protect -o output.pdf -p mypassword input.pdf
```

*   `-o`, `--output`: Path to the output PDF file (required).
*   `-p`, `--password`: Password to add (required).
*   `input`: Path to the input PDF file (required).

#### `unprotect`

Remove a password from a PDF.

```bash
pdfcli unprotect -o output.pdf -p mypassword input.pdf
```

*   `-o`, `--output`: Path to the output PDF file (required).
*   `-p`, `--password`: Password to remove (required).
*   `input`: Path to the input PDF file (required).

#### `fromtext`

Create a PDF from a text file or raw text.

```bash
# From a text file
pdfcli fromtext --input input.txt -o output.pdf

# From raw text
pdfcli fromtext --text "Hello, this is raw text content." -o output.pdf
```

*   `--input`: Path to the input text file (optional, use with `--text`).
*   `--text`: Raw text content to convert to PDF (optional, use with `--input`).
*   `-o`, `--output`: Path to the output PDF file (required).

#### `fromimages`

Create a PDF from image files.

```bash
pdfcli fromimages -o output.pdf image1.png image2.jpg [image3.jpeg ...]
```

*   `-o`, `--output`: Path to the output PDF file (required).
*   `input`: Paths to the input image files (one or more, required).

#### `extracttext`

Extract text from a PDF file.

```bash
pdfcli extracttext -o output.txt input.pdf
```

*   `-o`, `--output`: Path to the output text file (required).
*   `input`: Path to the input PDF file (required).

#### `watermark`

Add a watermark to a PDF file.

```bash
pdfcli watermark -o output.pdf -w watermark.pdf input.pdf
```

*   `-o`, `--output`: Path to the output PDF file (required).
*   `-w`, `--watermark`: Path to the watermark PDF file (required).
*   `input`: Path to the input PDF file (required).

#### `reorder`

Reorder pages in a PDF file.

```bash
pdfcli reorder -o output.pdf -p 3,1,2 input.pdf
```

*   `-o`, `--output`: Path to the output PDF file (required).
*   `-p`, `--pages`: Comma-separated new order of pages (e.g., `3,1,2` to make page 3 the first, page 1 the second, and page 2 the third).
*   `input`: Path to the input PDF file (required).

#### `compress`

Compress a PDF file.

```bash
pdfcli compress -o compressed.pdf input.pdf
```

*   `-o`, `--output`: Path to the output compressed PDF file (required).
*   `input`: Path to the input PDF file (required).

#### `extractimages`

Extract images from a PDF file.

```bash
pdfcli extractimages -o output_directory input.pdf
```

*   `-o`, `--output`: Path to the output directory for images (required).
*   `input`: Path to the input PDF file (required).

#### `toimages`

Convert PDF pages to image files.

```bash
pdfcli toimages -o output_directory input.pdf
pdfcli toimages -o output_directory -z 3 input.pdf # With a zoom factor
```

*   `-o`, `--output`: Path to the output directory for images (required).
*   `-z`, `--zoom`: Zoom factor for image conversion (default: 2). Higher values result in higher resolution images.
*   `input`: Path to the input PDF file (required).

#### `deletepages`

Delete specific pages from a PDF file.

```bash
pdfcli deletepages -o output.pdf -p 2,4 input.pdf
```

*   `-o`, `--output`: Path to the output PDF file (required).
*   `-p`, `--pages`: Comma-separated page numbers to delete (e.g., `2,4` to delete page 2 and page 4).
*   `input`: Path to the input PDF file (required).

## Development

### Running Tests

To run all unit tests:

```bash
python -m unittest discover tests
```

To run a specific test file:

```bash
python -m unittest tests/test_merge.py
```

### Building Executables (Local)

To build a standalone executable for your current OS:

```bash
pyinstaller --onefile --name pdfcli pdfcli/main.py
```

The executable will be found in the `dist/` directory.

## GitHub Actions

This project uses GitHub Actions for continuous integration and continuous delivery (CI/CD). The workflows are defined in the `.github/workflows/` directory.

### `main.yml`

This workflow performs the following actions:

*   **Tests**: Runs unit tests on `ubuntu-latest`, `windows-latest`, and `macos-latest` environments.
*   **Build & Bundle**: Creates standalone executables for `ubuntu-latest`, `windows-latest`, and `macos-latest` using PyInstaller.
*   **Release**: Creates a GitHub Release with the bundled executables when a new tag is pushed.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.