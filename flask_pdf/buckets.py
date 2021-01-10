from PyPDF2 import PdfFileReader as reader
import json


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


pdf_document = "books/Diestel-Graph-Theory.pdf"

ranks = {
    "24": 0.03203812069260971,
    "2pn": 0.030038120692609707,
    "a connected bipartite planar graph": 0.054144565831749134,
    "a connected planar graph": 0.05433579105339363,
    "a graph g": 0.05306214773645747,
    "a maximal planar graph": 0.052744650808571034,
    "bipartite": 0.014038120692609695,
    "bipartite planar graph": 0.07968906870517212,
    "cid": 0.03203812069260971,
    "cid:24)= g": 0.0625261766450238,
    "circuit": 0.0220381206926097,
    "circuit c 0k": 0.057425486546874585,
    "connected": 0.014038120692609695,
    "drawing": 0.024038120692609702,
    "edges": 0.012038120692609695,
    "faces": 0.010038120692609695,
    "g 0": 0.060452924119061835,
    "g 0k": 0.06860332093169687,
    "g 0n": 0.060452924119061835,
    "graph": 0.0060381206926096945,
    "graphs": 0.024038120692609702,
    "m edges": 0.05394934383053046,
    "maximal": 0.0060381206926096945,
    "most 2pn vertices": 0.06126486037845548,
    "planar": 0.0060381206926096945,
    "planar graphs": 0.0729825352962936,
    "planar graphs drawing": 0.059105738361320305,
    "point": 0.016038120692609695,
    "point p": 0.05416443263161068,
    "points": 0.0040381206926096945,
    "vertices": 0.030038120692609707
}

to_search = list(ranks.keys())

buckets = dict()


def get_bucket_score(bucket_words, ranks_dict):
    score = 0
    for word in bucket_words:
        score += ranks_dict[word]
    return score


with open(pdf_document, "rb") as file_handle:
    pdf = reader(file_handle)
    pages = pdf.getNumPages()

    print("Number of pages: %i" % pages)

    print("Starting analyzing book...")

    words_cluster = list()
    first_page_of_cluster = 80

    no_of_empty_pages = 0
    for page_number in range(10, pages - 50):
        page = pdf.getPage(page_number)
        page_text = page.extractText()

        is_page_empty = True
        number_of_words_on_current_page = 0

        for word in to_search:
            if word.lower() in page_text.lower():
                number_of_words_on_current_page += 1
                if len(words_cluster) == 0:
                    first_page_of_cluster = page_number + 1
                no_of_empty_pages = 0
                for i in range(page_text.lower().count(word.lower())):
                    words_cluster.append(word)

        if number_of_words_on_current_page > int(len(to_search) * 0.1):
            is_page_empty = False

        if is_page_empty:
            no_of_empty_pages += 1

        if no_of_empty_pages == 1:
            last_page_of_cluster = page_number
            buckets[f"{first_page_of_cluster}-{last_page_of_cluster}"] = words_cluster
            words_cluster = list()

        # print(f'Current buckets: {buckets}')

    # print(f'\nBuckets: {json.dumps(buckets, indent=2, cls=SetEncoder)}')

    sorted_words = sorted(buckets.items(), key=lambda item: get_bucket_score(item[1], ranks), reverse=True)
    no_of_buckets = int(len(sorted_words) * 0.1)
    for index, bucket in enumerate(sorted_words):
        print(f'Bucket: {bucket[0]} with score {get_bucket_score(bucket[1], ranks)}')
        if index > no_of_buckets:
            break
