#!/usr/bin/python

import argparse
import os
from PyPDF2 import PdfFileWriter, PdfFileReader


def create_parsers():
    parser = argparse.ArgumentParser(
        prog='split',
        description='"%(prog)s" slices a given pdf file into 1 pdf per page',
    )

    parser.add_argument(
        '-i', '--input',
        type=str,
        required=True,
        help='Input pdf to slice',
    )

    return parser


def split(input_pdf):
    output_filename = os.path.splitext(input_pdf)[0]
    output_extension = os.path.splitext(input_pdf)[-1]

    input_pdf = PdfFileReader(open(input_pdf, 'rb'))

    for i in range(input_pdf.numPages):
        output = PdfFileWriter()
        output.addPage(input_pdf.getPage(i))

        with open(output_filename + "-page" + str(i) + output_extension, 'wb') as output_stream:
            output.write(output_stream)


if __name__ == '__main__':

    p = create_parsers()
    args = p.parse_args()

    input_filename = args.input

    split(input_filename)
