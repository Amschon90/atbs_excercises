import PyPDF2, os

os.chdir('C:\\Users\\Zig0n\\Documents\\VSCode Projects\\atbs_excercises\\Ch_14')

pdfFile = open('AmSchonResume.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfWriter.encrypt('BEAR')
resultPdf = open('AmSchonResume_encrypted.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()