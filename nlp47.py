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


def out_from_to(chunks):

    for idx, c in enumerate(chunks):
        # この文節の番号 この文節の文字列 かかり先番号 かかり先文節
        kakarimoto_txt = str(c).replace('。', '').replace('、', '')

        kakarisaki_txt = ''
        if int(c.dst) > 0:
            kakarisaki_txt = str(chunks[int(c.dst)]).replace('。', '').replace('、', '')

        print(idx, kakarimoto_txt, c.dst, kakarisaki_txt, sep='\t')


def out_meishi_to_doushi(chunks):
    # 名詞を含む文節が、動詞を含む文節に係るものを出力

    for idx, c in enumerate(chunks):

        # 係り元（カレントの）判定
        # todo:イテレータ/ジェネレータでの実装
        kakarimoto_pos = [x.pos for x in c.morphs]
        if '名詞' not in kakarimoto_pos:
            # カレントの文節が、名詞を含まない
            continue
        kakarimoto_txt = str(c).replace('。', '').replace('、', '')

        # 係り先の判定
        if int(c.dst) > 0:
            kakarisaki = chunks[int(c.dst)]
            kakarisaki_pos = [x.pos for x in kakarisaki.morphs]
            if '動詞' not in kakarisaki_pos:
                # 係り先文節が、動詞を含まない
                continue
            kakarisaki_txt = str(chunks[int(c.dst)]).replace('。', '').replace('、', '')
        else:
            # 係り先無し
            continue

        # この文節の番号 この文節の文字列 かかり先番号 かかり先文節
        print(idx, kakarimoto_txt, c.dst, kakarisaki_txt, sep='\t')


def visualization(chunks):
    # 係り方をタプルのリストにして、グラフ表示
    chunks_tree = []

    for idx, c in enumerate(chunks):

        # 係り元（カレントの）判定
        # todo:イテレータ/ジェネレータでの実装
        # kakarimoto_pos = [x.pos for x in c.morphs]
        # if '名詞' not in kakarimoto_pos:
        #     # カレントの文節が、名詞を含まない
        #     continue
        kakarimoto_txt = str(c).replace('。', '').replace('、', '')

        # 係り先の判定
        if int(c.dst) > 0:
            kakarisaki = chunks[int(c.dst)]
            kakarisaki_pos = [x.pos for x in kakarisaki.morphs]
            # if '動詞' not in kakarisaki_pos:
            #     # 係り先文節が、動詞を含まない
            #     continue
            kakarisaki_txt = str(chunks[int(c.dst)]).replace('。', '').replace('、', '')
        else:
            # 係り先無し
            continue

        # この文節の番号 この文節の文字列 かかり先番号 かかり先文節
        # print(idx, kakarimoto_txt, c.dst, kakarisaki_txt, sep='\t')
        chunks_tree.append((kakarimoto_txt, kakarisaki_txt))

    g = pydot.graph_from_edges(chunks_tree)

    g = graphviz.Digraph(format='jpg')
    g.edges(chunks_tree)
    g.render('chunks_tree')


def kaku_pattern(chunks):

    # 係り方をタプルのリストにして、グラフ表示
    result_zyoshi = {}
    result_zyutsugo = {}
    for idx, c in enumerate(chunks):
        # 係り先の判定
        if int(c.dst) > 0:
            kakarisaki = chunks[int(c.dst)]
            kakarisaki_pos = [x.pos for x in kakarisaki.morphs]
            kakarisaki_base = [x.base for x in kakarisaki.morphs]
            if '動詞' not in kakarisaki_pos:
                # 係り先文節が、動詞を含まない
                continue
            else:
                # かかり先なし
                doushi_idx = kakarisaki_pos.index('動詞')
                kakarisaki_txt = kakarisaki_base[doushi_idx]


        # 係り元（カレントの）判定
        kakarimoto_pos = [x.pos for x in c.morphs]
        if '助詞' not in kakarimoto_pos:
            # カレントの文節が、動詞を含まない
            continue
        else:
            zyoshi_idx = kakarimoto_pos.index('助詞')
            zyoshi = c.morphs[zyoshi_idx].base
            result_zyoshi.setdefault(kakarisaki_txt, []).append(zyoshi)
            result_zyutsugo.setdefault(kakarisaki_txt, []).append(c)

    for k in result_zyoshi.keys():
        print(k + '\t', end='')
        for z in result_zyoshi[k]:
            print(z + '\t', end='')
        for y in result_zyutsugo[k]:
            print(str(y) + '\t', end='')
        print('\n')


def wo_kaku_pattern(chunks):


    zyutsugo = ''
    kakarisaki_txt = ''
    kakarimoto_idx = 0
    doushi_idx = -1
    dst = -1
    moto = -1
    for idx, c in enumerate(chunks):

        # 係り元（カレントの）判定
        kakarimoto_pos = [x.pos for x in c.morphs]
        kakarimoto_pos1 = [x.pos1 for x in c.morphs]
        if '名詞' not in kakarimoto_pos:
            # カレントの文節が、名詞を含まない
            continue
        elif 'サ変接続' not in kakarimoto_pos1:
            # カレントの文節が、サ変接続でない
            continue
        elif kakarimoto_pos1.index('サ変接続') + 1 == len(kakarimoto_pos1):
            continue

        elif not ((c.morphs[kakarimoto_pos1.index('サ変接続') + 1].pos == '助詞')
                and (c.morphs[kakarimoto_pos1.index('サ変接続') + 1].base == "を")):
            # サ変接続名詞に続く助詞が、'を' でない
            continue
        else:
            # 係り元の条件を満たす
            #pass
            #for w in c.morphs:
                #print(w)
            #print(len(kakarimoto_pos), kakarimoto_pos1.index('サ変接続'))
            #print(c.morphs[kakarimoto_pos1.index('サ変接続') + 1].base)
            kakarimoto_idx = kakarimoto_pos1.index('サ変接続')


        # 係り先の判定
        if int(c.dst) > 0:
            kakarisaki = chunks[int(c.dst)]
            kakarisaki_pos = [x.pos for x in kakarisaki.morphs]
            kakarisaki_base = [x.base for x in kakarisaki.morphs]
            if '動詞' not in kakarisaki_pos:
                # 係り先文節が、動詞を含まない
                continue
            else:
                # かかり先なし
                # 最左（idxの最小）の動詞を取る
                if (doushi_idx < 0) or (doushi_idx > 0 and doushi_idx < kakarisaki_pos.index('動詞')):
                    doushi_idx = kakarisaki_pos.index('動詞')
                    zyutsugo = c.morphs[kakarimoto_idx].base + c.morphs[kakarimoto_idx+1].base + kakarisaki_base[doushi_idx]
                    dst = int(c.dst)
                    moto = int(idx)



    #chunksすべてチェック後
    if zyutsugo:
        print(dst)
        print(moto)
        zyo = []
        setsu = []
        #test = []
        # todo:まだおかしい
        for idy, x in enumerate(chunks):
            if x.dst == str(dst) and idy != moto:
                setsu.append(str(x))
                for w in x.morphs:
                    if w.pos == '助詞' and w.pos1 == '格助詞':
                        zyo.append(w.surface)
        print(zyutsugo, zyo, setsu)




        #print(zyutsugo, [ str(y) for y in list(filter(lambda x: x.dst == str(dst), chunks))])




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
                        # out_meishi_to_doushi(chunks)
                        cnt = cnt + 1
                        wo_kaku_pattern(chunks)
                    #if cnt == 5:
                        #wo_kaku_pattern(chunks)
                        #visualization(chunks)
                        #for c in chunks:
                        #    print(c, end='\n\n')
                        # todo:全体にあてるとエラーが発生するchunksがある
                        # out_from_to(chunks)
                        #out_meishi_to_doushi(chunks)
                    chunks = []

            elif surface != 'EOS\n' and line[0] != '*':

                surface = line.split('\t')[0]
                olist = line.split('\t')[1].split(',')
                morph = Morph(surface, olist[6], olist[0], olist[1])
                chunk.morphs.append(morph)


if __name__ == '__main__':
    main()
