
import argparse
from .merge import merge_pdfs
from .split import split_pdf
from .rotate import rotate_pdf
from .protect import protect_pdf
from .unprotect import unprotect_pdf
from .fromtext import from_text
from .fromimages import from_images
from .extract_text import extract_text
from .watermark import add_watermark
from .reorder import reorder_pages
from .compress import compress_pdf
from .extract_images import extract_images
from .to_images import to_images
from .delete_pages import delete_pages

def main():
    parser = argparse.ArgumentParser(description='A feature-rich PDF CLI tool.')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Merge command
    merge_parser = subparsers.add_parser('merge', help='Merge multiple PDF files into one.')
    merge_parser.add_argument('input', nargs='+', help='Paths to the input PDF files.')
    merge_parser.add_argument('-o', '--output', required=True, help='Path to the output PDF file.')

    # Split command
    split_parser = subparsers.add_parser('split', help='Split a PDF into multiple files.')
    split_parser.add_argument('input', help='Path to the input PDF file.')
    split_parser.add_argument('-o', '--output', required=True, help='Output path prefix.')
    split_parser.add_argument('-r', '--ranges', nargs='+', required=True, help='Page ranges to split (e.g., 1-5 6-10).')

    # Rotate command
    rotate_parser = subparsers.add_parser('rotate', help='Rotate pages in a PDF.')
    rotate_parser.add_argument('input', help='Path to the input PDF file.')
    rotate_parser.add_argument('-o', '--output', required=True, help='Path to the output PDF file.')
    rotate_parser.add_argument('-r', '--rotation', type=int, required=True, help='Rotation angle in degrees (e.g., 90, 180, 270).')

    # Protect command
    protect_parser = subparsers.add_parser('protect', help='Add a password to a PDF.')
    protect_parser.add_argument('input', help='Path to the input PDF file.')
    protect_parser.add_argument('-o', '--output', required=True, help='Path to the output PDF file.')
    protect_parser.add_argument('-p', '--password', required=True, help='Password to add.')

    # Unprotect command
    unprotect_parser = subparsers.add_parser('unprotect', help='Remove a password from a PDF.')
    unprotect_parser.add_argument('input', help='Path to the input PDF file.')
    unprotect_parser.add_argument('-o', '--output', required=True, help='Path to the output PDF file.')
    unprotect_parser.add_argument('-p', '--password', required=True, help='Password to remove.')

    # From Text command
    fromtext_parser = subparsers.add_parser('fromtext', help='Create a PDF from a text file.')
    fromtext_parser.add_argument('input', help='Path to the input text file.')
    fromtext_parser.add_argument('-o', '--output', required=True, help='Path to the output PDF file.')

    # From Images command
    fromimages_parser = subparsers.add_parser('fromimages', help='Create a PDF from image files.')
    fromimages_parser.add_argument('input', nargs='+', help='Paths to the input image files.')
    fromimages_parser.add_argument('-o', '--output', required=True, help='Path to the output PDF file.')

    # Reorder command
    reorder_parser = subparsers.add_parser('reorder', help='Reorder pages in a PDF file.')
    reorder_parser.add_argument('input', help='Path to the input PDF file.')
    reorder_parser.add_argument('-o', '--output', required=True, help='Path to the output PDF file.')
    reorder_parser.add_argument('-p', '--pages', required=True, help='Comma-separated new order of pages (e.g., 1,3,2,4).')

    args = parser.parse_args()

    if args.command == 'merge':
        merge_pdfs(args.input, args.output)
    elif args.command == 'split':
        split_pdf(args.input, args.output, args.ranges)
    elif args.command == 'rotate':
        rotate_pdf(args.input, args.output, args.rotation)
    elif args.command == 'protect':
        protect_pdf(args.input, args.output, args.password)
    elif args.command == 'unprotect':
        unprotect_pdf(args.input, args.output, args.password)
    elif args.command == 'fromtext':
        from_text(args.output, input_path=args.input, text_content=args.text)
    elif args.command == 'fromimages':
        from_images(args.input, args.output)
    elif args.command == 'extracttext':
        extract_text(args.input, args.output)
    elif args.command == 'watermark':
        add_watermark(args.input, args.watermark, args.output)
    elif args.command == 'reorder':
        reorder_pages(args.input, args.output, args.pages)
    elif args.command == 'compress':
        compress_pdf(args.input, args.output)
    elif args.command == 'extractimages':
        extract_images(args.input, args.output)
    elif args.command == 'toimages':
        to_images(args.input, args.output, args.zoom)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
