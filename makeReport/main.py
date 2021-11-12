import json
from docx2pdf import convert
from PyPDF2 import PdfFileMerger

from converter import convert

if __name__ == '__main__':
    with open('config.json', 'r') as f:
        config = json.load(f)

    merger = PdfFileMerger()

    header_pdf = str(config['header'])
    position = header_pdf.rfind(".")
    header_pdf = header_pdf[:position] + ".pdf"

    #convert(config['header'], pdf_name)
    convert(config['header'], header_pdf)

    files = [header_pdf, config['body']]

    for pdf in files:
        merger.append(pdf)

    merger.write(config['output'])
    merger.close()
