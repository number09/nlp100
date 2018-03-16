import json
import re


def main():

    reg = re.compile(r'\'{2,}')
    #reg_link = re.compile(r'(\[{2,}|\]{2,})')
    reg_link = re.compile(r'''
        \[{2}
        (?:
            [^|]*?
            \|
        )?
        ([^|]*?)
        \]{2}
    ''')

    with open('jawiki-country.json' ,'r') as infile:
        for line in infile:
            jdic = json.loads(line)
            if jdic['title'] == 'イギリス':
                dic = dict(re.findall(r'\|(\w+)\s\=\s(.+)' ,jdic['text'] ,re.I))
                # print(dic)
                for k, v in dic.items():
                    print(k, dic[k])
                    dic[k] = reg.sub('', v)
                    dic[k] = reg_link.sub(r'\1', dic[k])
                    print(k, dic[k])


if __name__ == '__main__':
    main()
