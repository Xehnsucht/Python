from PyPDF2 import PdfFileMerger
import os
import zipfile as zp

os.chdir('D:\Book\PyForBooks')
pdfs = ['INF.pdf', 'INF0.pdf', 'INF1.pdf',
        'INF2.pdf', 'INF3.pdf', 'INF4.pdf',
        'INF5.pdf', 'INF6.pdf', 'INF7.pdf',
        'INF8.pdf', 'INF9.pdf', 'INF10.pdf',
        'INF11.pdf', 'INF12.pdf', 'INF13.pdf',
        'INF14.pdf', 'INF15.pdf', 'INF16.pdf'
        ]

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("ElectronBook.pdf")
archive = zp.ZipFile('ElectronBook.zip', mode='w')

for _ in pdfs:
    archive.write(_)
archive.close()
