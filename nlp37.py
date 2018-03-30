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
    x = []
    y = []
    for ix, w in enumerate(sorted(allwords.items(), key=lambda x:x[1], reverse=True)):
        if ix >= 10:
            break
        else:
            x.append(w[0])
            y.append(w[1])

    plt.bar(x, y)
    plt.show()


if __name__ == '__main__':
    main()
