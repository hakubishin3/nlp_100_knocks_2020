"""
36. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
"""
import pandas as pd
import matplotlib.pyplot as plt


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
answer = pd.Series(surfaces).value_counts().sort_values(ascending=False).head(10)
plt.bar(answer.index, answer.values)
plt.show()
