"""
41. 係り受け解析結果の読み込み（文節・係り受け）
40に加えて，文節を表すクラスChunkを実装せよ．
このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
さらに，入力テキストの係り受け解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，冒頭の説明文の文節の文字列と係り先を表示せよ．
本章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

"""
https://github.com/upura/nlp100v2020/blob/master/ch05/ans41.py
"""
class Morph:
    def __init__(self, dc):
        self.surface = dc['surface']
        self.base = dc['base']
        self.pos = dc['pos']
        self.pos1 = dc['pos1']


class Chunk:
    def __init__(self, dst):
        self.morphs = []        # 形態素（Morphオブジェクト）のリスト
        self.dst = dst          # 係り先文節インデックス番号
        self.srcs = []          # 係り元文節インデックス番号のリスト
        self.idx = None         # インデックス番号

def parse_cabocha(block):
    res = []
    chunk_generage_flg = 0
    for line in block.split("\n"):
        if line == "":
            res.append(chunk)
        elif line[0] == "*":
            if chunk_generage_flg == 1:
                res.append(chunk)
            dst = line.split(" ")[2].rstrip("D")
            chunk = Chunk(dst=dst)
            chunk_generage_flg = 1
        else:
            (surface, attr) = line.split("\t")
            attr = attr.split(",")
            lineDict = {
                'surface': surface,
                'base': attr[6],
                'pos': attr[0],
                'pos1': attr[1]
            }
            morph = Morph(lineDict)
            chunk.morphs.append(morph)

    for i, r in enumerate(res):
        res[int(r.dst)].srcs.append(i)
        res[i].idx = i

    return res


file = "./data/ai.ja.txt.cabocha"
with open(file, "r") as f:
    blocks = f.read().split("EOS\n")
blocks = list(filter(lambda x: x != '', blocks))
blocks = [parse_cabocha(block) for block in blocks]

for block in blocks[:10]:
    for m in block:
        print(m.idx, [i.surface for i in m.morphs], m.dst, m.srcs)
    print("\n")
