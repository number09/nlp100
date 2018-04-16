import re
import xml.etree.ElementTree as ET


def main():

    tree = ET.parse('nlp.txt.xml')

    root = tree.getroot()

    for token in root.iter('token'):
        for sub in token.iter():
            word = lemma = pos = ''
            # todo:もう少しいい検索の方法を調べる
            if sub.find('word') is not None:
                word = sub.find('word').text
            if sub.find('lemma') is not None:
                lemma = sub.find('lemma').text
            if sub.find('POS') is not None:
                pos = sub.find('POS').text
            if word and lemma and pos:
                print(word, lemma, pos, sep='\t')


if __name__ == '__main__':
    main()
