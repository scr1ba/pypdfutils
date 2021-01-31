#!/usr/bin/python

import argparse
import os

from PyPDF2 import PdfFileReader, PdfFileWriter


def create_parsers():
    parser = argparse.ArgumentParser(
        prog='drop',
        description='"%(prog)s" removes specified pages from given pdf',
    )

    parser.add_argument(
        '-i', '--input',
        type=str,
        required=True,
        help='Input pdf',
    )

    parser.add_argument(
        '-p', '--pages',
        type=int,
        nargs='+',
        required=True,
        help='Pages to remove, index starts at 0',
    )

    return parser


def drop(input_pdf, pages_to_delete):
    pdf = PdfFileReader(input_pdf, 'rb')
    output_pdf = PdfFileWriter()
    output_pdf_filename = os.path.splitext(input_pdf)[0]
    output_pdf_extension = os.path.splitext(input_pdf)[-1]

    for i in range(pdf.getNumPages()):
        if i not in pages_to_delete:
            output_pdf.addPage(pdf.getPage(i))

    with open(output_pdf_filename + "-trimmed" + output_pdf_extension, 'wb') as output_stream:
        output_pdf.write(output_stream)


if __name__ == '__main__':

    p = create_parsers()
    args = p.parse_args()

    input_filename = args.input
    pages_to_drop = args.pages

    if len(input_filename) < 1:
        raise Exception("Input must contain only one document")

    drop(input_filename, pages_to_drop)
