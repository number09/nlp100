import json
import pymongo


def main():

    client = pymongo.MongoClient()
    nlp_db = client.nlp
    collection = nlp_db.nlpcollection

    # todo:bulkもできるっぽい
    with open('artist.json', 'r') as f:
        for line in f:
            j = json.loads(line)

            collection.insert_one(j)

    # collection.create_index([("name", pymongo.ASCENDING), ("aliases.name", pymongo.ASCENDING), ("tags.value", pymongo.ASCENDING), ("rating.value", pymongo.ASCENDING)])


if __name__ == '__main__':
    main()
