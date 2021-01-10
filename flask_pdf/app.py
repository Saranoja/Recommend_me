from flask import Flask, request, jsonify
import os
import re
from pdfminer.high_level import extract_text
import io
import keywords_retriever

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

    keywords_set = keywords_retriever.get_keywords(text)

    return jsonify(list(keywords_set)), 200


app.run()
