import pydot
import graphviz


class Morph:

    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return '_'.join([self.surface, self.base, self.pos, self.pos1])


class Chunk:

    def __init__(self, dst, srcs, morphs):

        self.dst = dst
        self.srcs = srcs
        self.morphs = morphs

    def __str__(self):
        st = []
        for m in self.morphs:
            st.append(m.surface)
        return ''.join(st)


def meishi_to_root(chunks):
    # 名詞から根へのパス抽出


    for idx, c in enumerate(chunks):

        path = []

        # 係り元（カレントの）判定
        kakarimoto_pos = [x.pos for x in c.morphs]
        if '名詞' not in kakarimoto_pos:
            # カレントの文節が、名詞を含まない
            continue
        else:
            get_dst(chunks, idx, path)
        print(' -> '.join(path))


def get_dst(chunks, index, path):
    chunk = chunks[index]
    path.append(str(chunk))
    if int(chunk.dst) > 0:
        get_dst(chunks, int(chunk.dst), path)





def main():

    cnt = 0
    chunk = None
    dst = None
    srcs = []
    morphs = []
    chunks = []

    with open('neko.txt.cabocha', 'r') as infile:
        for idx, line in enumerate(infile):
            surface = line.split(' ')[0]

            if surface == 'EOS\n' or line[0] == '*':

                if len(morphs) > 1:
                    chunk = Chunk(morphs, dst, srcs)

                srcs = []
                morphs = []
                dst = None

                if surface == '*':

                    if chunk:
                        chunks.append(chunk)

                    # Chunk Header
                    chunk = Chunk('', [], [])
                    dst = line.split(' ')[2]
                    chunk.dst = dst.strip('D')

                    srcs.append(line.split(' ')[1])
                else:
                    # EOS
                    chunks.append(chunk)

                    chunk = None

                    # sentence
                    if len(chunks) > 1:
                        cnt = cnt + 1
                    if cnt == 5:
                        meishi_to_root(chunks)
                        # todo:全体にあてるとエラーが発生するchunksがある
                    chunks = []

            elif surface != 'EOS\n' and line[0] != '*':

                surface = line.split('\t')[0]
                olist = line.split('\t')[1].split(',')
                morph = Morph(surface, olist[6], olist[0], olist[1])
                chunk.morphs.append(morph)


if __name__ == '__main__':
    main()
