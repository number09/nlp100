import json
import redis


def main():
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    r = redis.StrictRedis(connection_pool=pool)

    with open('artist.json', 'r') as f:
        for line in f:
            print(line)
            j = json.loads(line)
            print(j)

            r.set(j['name'], j.get('area', ''))


if __name__ == '__main__':
    main()
