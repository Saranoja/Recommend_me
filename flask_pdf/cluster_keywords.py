"""
in: keywords set
out: best cluster (range-like) found in text
"""

import spacy
import pytextrank

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

keywords = []
for p in doc._.phrases:
    # print("{}".format(p.text))
    keywords.append(p.text)
    k += 1
    if k == 20:
        break

print(keywords)