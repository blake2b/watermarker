import PyPDF2

template = PyPDF2.PdfFileReader(open('INSERT_FILE_NAME', 'rb')) # File to watermark
watermark = PyPDF2.PdfFileReader(open('INSERT_FILE_NAME', 'rb')) # Watermark
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)