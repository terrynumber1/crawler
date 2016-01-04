import PyPDF2, os

pdfobject = open('mok.pdf' , 'rb')
pdfreader = PyPDF2.PdfFileReader(pdfobject)
pdfreader.numPages

print(pdfreader.numPages)

pageobject = pdfreader.getPage(0)
# print(pageobject.extractText())

array1=[]

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        array1.append(filename)

print('Array Content: ', array1)

array1.sort(key=str.lower)
print('Sorted Array Content: ', array1)

pdfwriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in array1:
    pdfobject = open(filename, 'rb')    # read, binary
    pdfreader = PyPDF2.PdfFileReader(pdfobject)

    print(pdfreader.getPage(1).extractText(), '--------------------------- END OF FILE -----------------------------')
    print('----------------------------------')
