#!/usr/bin/python

import argparse

from PyPDF2 import PdfFileMerger


def create_parsers():
    parser = argparse.ArgumentParser(
        prog='collate',
        description='"%(prog)s" collates pdfs',
    )

    parser.add_argument(
        '-i', '--input',
        type=str,
        nargs='+',
        required=True,
        help='Input pdf',
    )

    parser.add_argument(
        '-o', '--output',
        type=str,
        required=True,
        help='Output pdf',
    )

    return parser


def merge(inputs, output_path):
    merged_pdf = PdfFileMerger()
    for pdf in inputs:
        merged_pdf.append(pdf)

    with open(output_path, 'wb') as output_stream:
        merged_pdf.write(output_stream)


if __name__ == '__main__':

    p = create_parsers()
    args = p.parse_args()

    input_filename = args.input
    output_filename = args.output

    if len(input_filename) < 2:
        raise Exception("Input must contain more than one document")

    merge(input_filename, output_filename)
