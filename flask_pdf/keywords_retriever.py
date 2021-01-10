import pytextrank
import re
import spacy

word_tokenizer = re.compile("[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+")
with open("stopwords_english.txt", encoding="utf-8") as stopwords_file:
    stopwords_english = stopwords_file.read().split("\n")


def get_keywords(text, keywords_number=20):
    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm")

    # add PyTextRank to the spaCy pipeline
    tr = pytextrank.TextRank()
    nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)

    doc = nlp(text)

    # examine the top k-ranked phrases in the document
    keyword_sentences = [p.text for phrase_number, p in enumerate(doc._.phrases) if phrase_number < keywords_number]

    keywords_set = set()
    for keyword_sentence in keyword_sentences:
        for keyword in word_tokenizer.findall(keyword_sentence):
            if keyword not in stopwords_english:
                keywords_set.add(keyword)

    return keywords_set
