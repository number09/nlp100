import json
import pymongo


def main():


    client = pymongo.MongoClient()
    nlp_db = client.nlp
    collection = nlp_db.nlpcollection

    result = collection.find({}).sort("rating.count", -1).limit(10)
    for post in result:
        print(post)


if __name__ == '__main__':
    main()
