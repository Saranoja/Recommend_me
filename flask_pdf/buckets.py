from PyPDF2 import PdfFileReader as reader
from json import dumps
from collections import OrderedDict

key_phrases = ["mandatory access control models",
               "security classes",
               "mandatory integrity control",
               "security levels",
               "access control security policies",
               "mac models",
               "information ﬂow policies",
               "integrity classes",
               "information ﬂow",
               "integrity levels",
               "mandatory access control",
               "security label",
               "highest integrity",
               "class",
               "security classiﬁcation",
               "information",
               "security module",
               "security clearance",
               "models",
               "prevent information"]

to_search = set(keyword for phrase in key_phrases for keyword in phrase.split(" "))

print(f'Keywords to be searched in book: {to_search}')

pdf_document = "Introduction_to_Computer_Security.pdf"

buckets = dict()

with open(pdf_document, "rb") as file_handle:
    pdf = reader(file_handle)
    pages = pdf.getNumPages()

    print("number of pages: %i" % pages)

    print("Starting analyzing book...")

    words_cluster = set()
    first_page_of_cluster = 20

    for page_number in range(20, pages - 100):
        page = pdf.getPage(page_number)
        page_text = page.extractText()
        is_page_empty = True

        for word in to_search:
            if word in page_text:
                if len(words_cluster) == 0:
                    first_page_of_cluster = page_number
                is_page_empty = False
                words_cluster.add(word)

        if not is_page_empty:
            buckets[first_page_of_cluster] = words_cluster
        else:
            words_cluster.clear()

        print(f'Current buckets: {buckets}')

    print(f'\nBuckets: {buckets}')
    #
    # sorted_words = OrderedDict(sorted(buckets.items(), key=lambda item: len(item[1]), reverse=True))
    #
    # print(f'Sorted words: {sorted_words}')
    #
    # best5 = 0
    # best_5_clusters = {}
    # for k, v in sorted_words:
    #     best_5_clusters[k] = v
    #     best5 += 1
    #     if best5 == 5:
    #         break
    #
    # print(f'\nBest 5 clusters are found starting from pages: {best_5_clusters}')
