# from pymongo import MongoClient
#
# client = MongoClient("mongodb+srv://saranoja:saranoja@cluster0.pgzyu.mongodb.net/<dbname>?retryWrites=true&w=majority")
# db = client.recommend_me
# books_collection = db.books
# cursor = books_collection.find({})
# for document in cursor:
#     print(document)
import json


def get_books_on_subject(subject):
    with open('books.json') as books_file:
        books_json = json.loads(books_file.read())
        books = [book['name'] for book in books_json if book['subject'] == subject]
        return books
