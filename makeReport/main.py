import json
import sys

from PyPDF2 import PdfFileMerger

if __name__ == '__main__':
    with open('config.json', 'r') as f:
        config = json.load(f)

    merger = PdfFileMerger()

    files = [config['header'], config['body']]

    for pdf in files:
        merger.append(pdf)

    merger.write(config['output'])
    merger.close()
