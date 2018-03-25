

def main():

    sentence = []
    doushi = set()
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
                if word['pos'] == '動詞':
                    doushi.add(word['surface'])
            else:
                sentence = []
        else:
            sentence = []

    for w in doushi:
        print(w)

if __name__ == '__main__':
    main()
