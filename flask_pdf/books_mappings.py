# from pymongo import MongoClient
#
# client = MongoClient("mongodb+srv://saranoja:saranoja@cluster0.pgzyu.mongodb.net/<dbname>?retryWrites=true&w=majority")
# db = client.recommend_me
# books_collection = db.books
# cursor = books_collection.find({})
# for document in cursor:
#     print(document)
import json
from typing import List


def get_books_from_subject(subject: str) -> List[str]:
    with open('books.json') as books_file:
        books_json = json.loads(books_file.read())
        for dictionary in books_json:
            if subject.lower() in dictionary["subjects"]:
                return dictionary["books"]
            # books = [d['name'] for d in books_json if d['subject'] == subject]
