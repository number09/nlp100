import json
import pymongo


def main():

    in_aliase = input("input aliase name :")

    client = pymongo.MongoClient()
    nlp_db = client.nlp
    collection = nlp_db.nlpcollection

    result = collection.find({'aliases.name': in_aliase.strip()})
    for post in result:
        print(post)


if __name__ == '__main__':
    main()
