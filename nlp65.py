import json
import pymongo


def main():

    client = pymongo.MongoClient()
    nlp_db = client.nlp
    collection = nlp_db.nlpcollection

    result = collection.find_one({'name': 'Queen'})
    print(result)

if __name__ == '__main__':
    main()
