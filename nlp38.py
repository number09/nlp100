from matplotlib import pyplot as plt
from matplotlib import font_manager as fm

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
    data = []
    for w in allwords.values():
        data.append(w)

    plt.hist(data, range=(100, 15000))
    plt.show()


if __name__ == '__main__':
    main()
