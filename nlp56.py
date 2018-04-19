import re
import xml.etree.ElementTree as ET


def main():

    tree = ET.parse('nlp.txt.xml')

    root = tree.getroot()



    conf = {}
    for doc in root:
        for coref in doc.findall('coreference'):
            for mago in coref.findall('coreference'):
                ignore_sentence_no = 0
                ref_text = ''

                for men in mago:
                    if men.attrib.get('representative','') == 'true':
                        #print(men.find('text').text)
                        ignore_sentence_no = int(men.find('sentence').text)
                        ref_text = men.find('text').text

                for men in mago.findall('mention'):
                    if ignore_sentence_no != int(men.find('sentence').text):
                        conf[men.find('sentence').text + '-' + men.find('start').text + '-start'] = ref_text + "("
                        conf[men.find('sentence').text + '-' + str(int(men.find('end').text) - 1) + '-end'] = ")"

    #print(conf)

    document = root[0][1]

    #for sentence in root.iter('sentence'):
    for sentence in document.iter('sentence'):
        # todo:error
        sentence_id = sentence.attrib["id"]
        for token in sentence.iter('token'):
            token_id = token.attrib["id"]
            for sub in token.iter():
                word = lemma = pos = ner = speaker = ''
                # todo:もう少しいい検索の方法を調べる
                if sub.find('word') is not None:
                    word = sub.find('word').text
                if sub.find('lemma') is not None:
                    lemma = sub.find('lemma').text
                if sub.find('POS') is not None:
                    pos = sub.find('POS').text

                if word:
                    if (sentence_id + '-' + token_id + '-start') in conf:
                        print(conf[sentence_id + '-' + token_id + '-start'], end='')

                    print(word, end='')

                    if (sentence_id + '-' + token_id + '-end') in conf:
                        print(conf[sentence_id + '-' + token_id + '-end'], end='')
                    print(' ', end='')


        print('')



if __name__ == '__main__':
    main()
