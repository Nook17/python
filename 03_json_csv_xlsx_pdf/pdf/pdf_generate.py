#!/usr/bin/env python3
from weasyprint import CSS, HTML


def main():
    url = 'https://www.biznesradar.pl/'
    pdf_file = 'quarter.pdf'
    generate_pdf(url, pdf_file)


def generate_pdf(url, pdf_file):
    print('Generate pdf file')
    css = CSS(string='body{ font-size: 6px; }')
    HTML(url).write_pdf(pdf_file, stylesheets=[css])


if __name__ == '__main__':
    main()