import os
import win32com.client

wdFormatPDF = 17


def convert(input, output):
    inputFile = os.path.abspath(input)
    outputFile = os.path.abspath(output)
    word = win32com.client.Dispatch('Word.Application')
    doc = word.Documents.Open(inputFile)
    doc.SaveAs(outputFile, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()


def generate_pdf_name(name):
    pdf_name = str(name)
    position = pdf_name.rfind(".")
    pdf_name = pdf_name[:position] + ".pdf"
    return pdf_name