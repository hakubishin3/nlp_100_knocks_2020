"""
35. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""
import pandas as pd


def parse(line: str) -> dict:
    surface, attr = line.split("\t")
    attr = attr.split(",")
    result = {
        "surface": surface,
        "base": attr[6],
        "pos": attr[0],
        "pos1": attr[1]
    }
    return result

file = "./data/neko.txt.mecab"
with open(file, "r") as f:
    lines = f.read().split("\n")
lines = list(filter(lambda x: x not in ["", "EOS"], lines))
morphemes = [parse(line) for line in lines]

surfaces = [morpheme["surface"] for morpheme in morphemes]
answer = pd.Series(surfaces).value_counts().sort_values(ascending=False)
print(answer)
