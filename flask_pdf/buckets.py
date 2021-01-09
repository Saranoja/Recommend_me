from PyPDF2 import PdfFileReader as reader
import json


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


# key_phrases = ["mandatory access control models",
#                "security classes",
#                "mandatory integrity control",
#                "security levels",
#                "access control security policies",
#                "mac models",
#                "information ﬂow policies",
#                "integrity classes",
#                "information ﬂow",
#                "integrity levels",
#                "mandatory access control",
#                "security label",
#                "highest integrity",
#                "class",
#                "security classiﬁcation",
#                "information",
#                "security module",
#                "security clearance",
#                "models",
#                "prevent information"]

key_phrases = ['domain names', 'domain name system', 'dns| domain types', 'name servers', 'name', 'dns name space',
               'official name', 'internet name domain', 'full path name', 'in-addr.arpa domain', 'dns| host',
               'in-addr.arpa domain hierarchy', 'multiple ip addresses', 'ip address', 'dns organization', 'dns|',
               'dns| idn', 'dns| queries', 'dns| getaddrinfo', 'dns| gethostbyaddr']

to_search = set(keyword for phrase in key_phrases for keyword in phrase.split(" "))

print(f'Keywords to be searched in book: {to_search}')

# pdf_document = "Introduction_to_Computer_Security.pdf"
pdf_document = "Computer_Networking _A_Top_Down_Approach.pdf"

buckets = dict()

# with open(pdf_document, "rb") as file_handle:
#     pdf = reader(file_handle)
#     page = pdf.getPage(1)
#     print(page.extractText())

with open(pdf_document, "rb") as file_handle:
    pdf = reader(file_handle)
    pages = pdf.getNumPages()

    print("number of pages: %i" % pages)

    print("Starting analyzing book...")

    words_cluster = list()
    first_page_of_cluster = 80

    no_of_empty_pages = 0
    for page_number in range(50, 500):
        page = pdf.getPage(page_number)
        page_text = page.extractText()

        is_page_empty = True
        for word in to_search:
            if word.lower() in page_text.lower():
                if len(words_cluster) == 0:
                    first_page_of_cluster = page_number + 1
                is_page_empty = False
                no_of_empty_pages = 0
                words_cluster.append(word)

        if is_page_empty:
            no_of_empty_pages += 1

        if no_of_empty_pages == 1:
            last_page_of_cluster = page_number
            buckets[f"{first_page_of_cluster}-{last_page_of_cluster}"] = words_cluster
            words_cluster = list()

        # print(f'Current buckets: {buckets}')

    print(f'\nBuckets: {json.dumps(buckets, indent=2, cls=SetEncoder)}')

    sorted_words = sorted(buckets.items(), key=lambda item: len(item[1]), reverse=True)
    no_of_buckets = int(len(sorted_words) * 0.1)
    for index, bucket in enumerate(sorted_words):
        print(bucket)
        if index > no_of_buckets:
            break
