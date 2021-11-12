import json
import os

from docx2pdf import convert
from PyPDF2 import PdfFileMerger

from converter import convert, generate_pdf_name

if __name__ == '__main__':
    with open('config.json', 'r') as f:
        config = json.load(f)

    merger = PdfFileMerger()

    header_pdf = str(config['header'])
    position = header_pdf.rfind(".")
    header_pdf = header_pdf[:position] + ".pdf"

    #convert(config['header'], pdf_name)
    convert(config['header'], generate_pdf_name(config['header']))

    path = str(config['source'])
    position = path.rfind("\\")
    folder = path[:position]
    name = path[position + 1:]
    os.chdir(folder)
    os.system(f"pdflatex {name}")

    #os.system("pdflatex " + config['source'])

    files = [header_pdf, generate_pdf_name(config['source'])]

    for pdf in files:
        merger.append(pdf)

    merger.write(config['output'])
    merger.close()

    os.remove(header_pdf)
