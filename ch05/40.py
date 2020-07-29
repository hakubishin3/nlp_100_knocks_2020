"""
日本語Wikipediaの「人工知能」に関する記事からテキスト部分を抜き出したファイルがai.ja.zipに収録されている.
この文章をCaboChaやKNP等のツールを利用して係り受け解析を行い，その結果をai.ja.txt.parsedというファイルに保存せよ.
このファイルを読み込み，以下の問に対応するプログラムを実装せよ.
$ cat data/ai.ja.txt | cabocha -f1 > data/ai.ja.txt.cabocha
"""

"""
40. 係り受け解析結果の読み込み（形態素）
形態素を表すクラスMorphを実装せよ．
このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．
さらに，係り受け解析の結果（ai.ja.txt.parsed）を読み込み，各文をMorphオブジェクトのリストとして表現し，冒頭の説明文の形態素列を表示せよ．
"""
class Morph:
    def __init__(self, parse_dict):
        self.surface = parse_dict["surface"]
        self.base = parse_dict["base"]
        self.pos = parse_dict["pos"]
        self.pos1 = parse_dict["pos1"]


def parse(line: str) -> dict:
    surface, attr = line.split("\t")
    attr = attr.split(",")
    result = {
        "surface": surface,
        "base": attr[6],
        "pos": attr[0],
        "pos1": attr[1]
    }
    return Morph(result)

file = "./data/ai.ja.txt.cabocha"
with open(file, "r") as f:
    lines = f.read().split("\n")
lines = list(filter(lambda x: x not in ["", "EOS"], lines))
morphemes = [parse(line) for line in lines if line[0] != "*"]
print(morphemes[:10])
