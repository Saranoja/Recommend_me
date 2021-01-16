from PyPDF2 import PdfFileReader as reader
import re

word_tokenizer = re.compile("[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+")


class ChaptersRetriever:
    def __init__(self, books_names, words_ranks):
        self.books_names = books_names
        self.words_ranks = words_ranks
        self.keyphrases = list(words_ranks.keys())

    def _get_bucket_score(self, bucket_words, ranks_dict):
        score = 0
        for word in bucket_words:
            score += ranks_dict[word]
        return score

    def _create_buckets(self, pdf_document: str):
        buckets = dict()
        with open(pdf_document, "rb") as file_handle:
            pdf = reader(file_handle)
            pages = pdf.getNumPages()

            print("Number of pages: %i" % pages)
            print("Starting analyzing book...")

            words_cluster = list()
            first_page_of_cluster = 10

            no_of_empty_pages = 0
            for page_number in range(10, pages - 50):
                page = pdf.getPage(page_number)
                page_text = page.extractText()
                total_words = len(word_tokenizer.findall(page_text))

                is_page_empty = True
                number_of_words_on_current_page = 0

                for word in self.keyphrases:
                    if word.lower() in page_text.lower():
                        number_of_words_on_current_page += 1
                        if len(words_cluster) == 0:
                            first_page_of_cluster = page_number + 1
                        no_of_empty_pages = 0
                        for i in range(page_text.lower().count(word.lower())):
                            words_cluster.append(word)

                if number_of_words_on_current_page > total_words * 0.03:
                    is_page_empty = False

                if is_page_empty:
                    no_of_empty_pages += 1

                if no_of_empty_pages == 1:
                    last_page_of_cluster = page_number
                    buckets[f"{first_page_of_cluster}-{last_page_of_cluster}"] = words_cluster
                    words_cluster = list()
            return buckets

    def get_top_chapters(self):
        chapters = dict()
        for book in self.books_names:
            pdf_document = f'books/{book}.pdf'
            buckets = self._create_buckets(pdf_document)
            sorted_words = sorted(buckets.items(), key=lambda item: self._get_bucket_score(item[1], self.words_ranks),
                                  reverse=True)
            if int(len(sorted_words) * 0.01) >= 2:
                no_of_buckets = int(len(sorted_words) * 0.01)
            else:
                no_of_buckets = 2
            top_buckets = [bucket[0] for index, bucket in enumerate(sorted_words) if index < no_of_buckets]
            chapters[book] = top_buckets
        return chapters
