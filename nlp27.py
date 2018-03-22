import json
import re


def main():

    reg = re.compile(r'\'{2,}')
    reg_link1 = re.compile(r'\[\[(?:[^\[\]:]+)\#(?:[^\[\]:]+)\|([^\[\]:]+)\]\]')
    reg_link2 = re.compile(r'\[\[(?:[^\[\]:]+)\|([^\[\]:]+)\]\]')
    reg_link3 = re.compile(r'\[\[([^\[\]:]+)\]\]')

    with open('jawiki-country.json' ,'r') as infile:
        for line in infile:
            jdic = json.loads(line)
            if jdic['title'] == 'イギリス':
                dic = dict(re.findall(r'\|(\w+)\s\=\s(.+)' ,jdic['text'] ,re.I))
                for k, v in dic.items():
                    print(k, dic[k])
                    dic[k] = reg.sub('', v)
                    dic[k] = reg_link1.sub(r'\1', dic[k])
                    dic[k] = reg_link2.sub(r'\1', dic[k])
                    dic[k] = reg_link3.sub(r'\1', dic[k])
                    print(k, dic[k])


if __name__ == '__main__':
    main()
