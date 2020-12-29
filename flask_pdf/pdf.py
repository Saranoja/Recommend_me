import os
import xml.etree.ElementTree as ET

# os.system("dumppdf.py --extract-toc --outfile=book-toc.xml --text-stream book.pdf")
os.system("pdf2txt.py --pagenos=1142 --outfile=book-pagenos.txt book.pdf")

# et = ET.parse("book-toc.xml")
# for e in et.getroot():
#     # print(e.items())
#     print(e.find("pageno").text)

# #!/usr/bin/env python3
# # parse_toc.py
#
# from pdfminer.pdfparser import PDFParser, PDFObjRef
# from pdfminer.pdfdocument import PDFDocument
#
# # PDFObjRef().resolve()
#
# def parse(filename, maxlevel):
#     fp = open(filename, 'rb')
#     parser = PDFParser(fp)
#     doc = PDFDocument(parser)
#
#     outlines = doc.get_outlines()
#     for t in outlines:
#         print(t)
#         por = t[2]
#         print(por[0])
#         print(por[0].resolve())
#         break
#     # for level, title, dest, a, se in outlines:
#     #     if level <= maxlevel:
#     #         title_words = title \
#     #             .encode('utf8') \
#     #             .replace('\n', '') \
#     #             .split()
#     #         title = ' '.join(title_words)
#     #         print(' ' * level, title)
#
#
# parse("book.pdf", 5)
# #
# # if __name__ == '__main__':
# #     import sys
# #
# #     if len(sys.argv) != 3:
# #         print('Usage: %s xxx.pdf level' % sys.argv[0])
# #         sys.exit(2)
# #
# #     parse(sys.argv[1], int(sys.argv[2]))
