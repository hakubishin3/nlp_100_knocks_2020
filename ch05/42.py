"""
42. 係り元と係り先の文節の表示
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
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

for block in blocks:
    for m in block:
        print("".join([i.surface for i in m.morphs]), "->", "".join([i.surface for i in block[int(m.dst)].morphs]))
