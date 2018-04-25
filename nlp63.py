import json
import redis


def main():
    pool = redis.ConnectionPool(host='localhost', port=6379, db=1)
    r = redis.StrictRedis(connection_pool=pool)

    with open('artist.json', 'r') as f:
        for line in f:
            j = json.loads(line)

            for tag in j.get('tags', []):
                if 'count' in tag and 'value' in tag:
                    r.hset(j['name'], tag['value'], tag['count'])



if __name__ == '__main__':
    main()
