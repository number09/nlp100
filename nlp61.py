import json
import redis


def main():

    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    r = redis.StrictRedis(connection_pool=pool)

    artist = input()

    print(r.get(artist))



if __name__ == '__main__':
    main()
