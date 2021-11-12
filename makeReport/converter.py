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
