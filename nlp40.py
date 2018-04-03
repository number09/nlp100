
class Morph:

    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return ','.join([self.surface, self.base, self.pos, self.pos1])


def main():

    sentence = []
    cnt = 0
    with open('neko.txt.cabocha', 'r') as infile:
        for idx, line in enumerate(infile):

            surface = line.split('\t')[0]

            if surface == 'EOS\n':
                cnt = cnt + 1
                if cnt/2 == 3:
                    for w in sentence:
                        print(w)

                sentence = []
            elif surface != 'EOS\n' and line[0] != '*':
                olist = line.split('\t')[1].split(',')
                word = Morph(surface, olist[6], olist[0], olist[1])
                sentence.append(word)
            else:
                pass


if __name__ == '__main__':
    main()
