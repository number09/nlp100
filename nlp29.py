import json
import re
import requests


def searchDictKey(dic, keyword):

    for key in dic.keys():
        if isinstance(dic[key], dict):
            searchDictKey(dic[key], keyword)
        elif isinstance(dic[key], list):
            for item in dic[key]:
                searchDictKey(item, keyword)
        else:
            if key == keyword:
                print('FIND!', dic[key])


def main():


    with open('jawiki-country.json', 'r') as infile:
        for line in infile:
            jdic = json.loads(line)
            if jdic['title'] == 'イギリス':
                dic = dict(re.findall(r'\|(\w+)\s\=\s(.+)' ,jdic['text'] ,re.I))

                search_title = dic['国旗画像']

                r = requests.get('https://www.mediawiki.org/w/api.php?'
                                 'action=query&format=json&titles='
                                 'File:{0}'
                                 '&prop=imageinfo&iiprop=url'.format(search_title))
                res = json.loads(r.text)
                searchDictKey(res, 'url')


if __name__ == '__main__':
    main()
