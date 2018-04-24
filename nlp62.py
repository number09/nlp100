import json
import redis


def main():

    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    r = redis.StrictRedis(connection_pool=pool)

    print(
        [r.get(k).decode('utf-8') for k in r.keys()].count('Japan')
    )


if __name__ == '__main__':
    main()
