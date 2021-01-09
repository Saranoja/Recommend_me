from flask import Flask, request, jsonify
import json
import requests
from bs4 import BeautifulSoup
import os
import re
import spacy
import pytextrank

# example text
with open("file.txt", encoding="utf-8") as file:
    text = file.read()

app = Flask(__name__)
word_tokenizer = re.compile("[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+")

with open("stopwords_english.txt") as stopwords_file:
    stopwords_english = stopwords_file.read().split("\n")


@app.route('/', methods=["POST"])
def PDF_to_word_occurrence():
    with open("file.pdf", "wb") as file:
        file.write(request.get_data())

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
    # write received file
    with open("file.pdf", "wb") as f:
        f.write(request.get_data())

    os.system('pdf2txt.py --outfile=file.txt --output_type=text file.pdf')

    # example text
    with open("file.txt", encoding="utf-8") as file:
        text = file.read()

    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm")

    # add PyTextRank to the spaCy pipeline
    tr = pytextrank.TextRank()
    nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)

    doc = nlp(text)

    # examine the top-ranked phrases in the document
    k = 0

    keyword_sentences = []
    for p in doc._.phrases:
        # print("{}".format(p.text))
        keyword_sentences.append(p.text)
        k += 1
        if k == 20:
            break

    keywords_set = set()
    for keyword_sentence in keyword_sentences:
        for keyword in word_tokenizer.findall(keyword_sentence):
            keywords_set.add(keyword)

    return jsonify(list(keywords_set)), 200


app.run()
