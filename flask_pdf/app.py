from flask import Flask, request, jsonify
import os
import re
from pdfminer.high_level import extract_text
import io
import keywords_retriever
import books_mappings
from buckets import ChaptersRetriever

app = Flask(__name__)


# endpoint not in use anymore@app.route('/', methods=["POST"])
def PDF_to_word_occurrence():
    with open("stopwords_english.txt", encoding="utf-8") as stopwords_file:
        stopwords_english = stopwords_file.read().split("\n")

    with open("file.pdf", "wb") as file:
        file.write(request.get_data())

    word_tokenizer = re.compile("[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+")
    os.system('pdf2txt.py --outfile=file.txt --output_type=text file.pdf')

    with open("file.txt") as file:
        words = file.read()
        words = word_tokenizer.findall(words)
        words = map(lambda word: word.lower(), words)
        words = filter(lambda word: word not in stopwords_english, words)
        words = list(words)

    occurrences = {}
    for word in words:
        if word not in occurrences:
            occurrences[word] = 1
        else:
            occurrences[word] += 1
    occurrences = dict(sorted(occurrences.items(), key=lambda x: x[1], reverse=True))
    print(occurrences)

    return jsonify(occurrences), 200


@app.route("/pdf_to_keywords", methods=["POST"])
def PDF_to_keywords():
    pdf_file = io.BytesIO(request.get_data())
    text = extract_text(pdf_file)

    keywords_set = keywords_retriever.get_keyphrases_rank(text)
    expanded_keywords_set = keywords_retriever.expand_keyphrases_dict(keywords_set)

    return jsonify(expanded_keywords_set), 200


@app.route("/further-reading/<subject_id>", methods=["POST"])
def get_further_reading(subject_id):
    pdf_file = io.BytesIO(request.get_data())
    pdf_text = extract_text(pdf_file)

    keyphrases_rank = keywords_retriever.get_keyphrases_rank(pdf_text)
    expanded_keyphrases_rank_set = keywords_retriever.expand_keyphrases_dict(keyphrases_rank)

    books = books_mappings.get_books_from_subject(subject_id)
    retriever = ChaptersRetriever(books, expanded_keyphrases_rank_set)
    top_reads = retriever.get_top_chapters()
    print(top_reads)

    return jsonify(top_reads), 200


app.run()
