

def main():

    sentence = []
    meishi = set()
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
                if word['pos'] == '名詞' and word['pos1'] == 'サ変接続':
                    meishi.add(word['surface'])
            else:
                sentence = []
        else:
            sentence = []

    for w in meishi:
        print(w)


if __name__ == '__main__':
    main()
