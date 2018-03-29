

def main():

    sentence = []
    allwords = {}
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

                allwords[surface] = allwords.get(surface, 0) + 1

            else:

                # 初期化
                sentence = []
    for w in sorted(allwords.items(), key=lambda x:x[1], reverse=True):
        print('{0:10}'.format(w[0]), '{0:10}'.format(w[1]))


if __name__ == '__main__':
    main()
