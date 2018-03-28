

def main():

    sentence = []
    with open('neko.txt.mecab', 'r') as infile:
        for idx, line in enumerate(infile):

            word = {}
            surface = line.split('\t')[0]
            if surface != 'EOS\n':
                olist = line.split('\t')[1].split(',')
                word['surface'] = surface
                word['base'] = olist[6]
                word['pos'] = olist[0]
                word['pos1'] = olist[1]

                sentence.append(word)
            else:
                for ix, w in enumerate(sentence):
                    if w['surface'] == 'の' and ix+1 != len(sentence):
                        if sentence[ix-1]['pos'] == '名詞' and sentence[ix+1]['pos'] == '名詞':
                            print(sentence[ix-1]['surface'], w['surface'], sentence[ix+1]['surface'])

                # 初期化
                sentence = []


if __name__ == '__main__':
    main()
