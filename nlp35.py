

def meishi_ren(sentence):
    renzoku_meishi = []
    for ix, w in enumerate(sentence):
        if w['pos'] == '名詞':
            renzoku_meishi.append(w['surface'])
        else:
            if len(renzoku_meishi) > 1:
                print(renzoku_meishi)
            renzoku_meishi = []
    else:
        if len(renzoku_meishi) !=0:
            print(renzoku_meishi)



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
                meishi_ren(sentence)

                # 初期化
                sentence = []


if __name__ == '__main__':
    main()
