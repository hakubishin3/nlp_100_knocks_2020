"""
34. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""
import numpy as np


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

x = np.array([1 if morpheme["pos"] == "名詞" else 0 for morpheme in morphemes])
temp = np.arange(len(morphemes))
temp[x > 0] = 0
np.maximum.accumulate(temp, out=temp)
left = temp
x_reversed = x[::-1]
temp = np.arange(len(morphemes))
temp[x_reversed > 0] = 0
np.maximum.accumulate(temp, out=temp)
right = len(x) - 1 - temp[::-1]
y = right - left + 1
y[x == 0] = 0

longest_consistent_idx = np.where(y == y.max())
answer = "".join([morpheme["surface"] for i, morpheme in enumerate(morphemes) if np.isin(i, longest_consistent_idx)])
print(answer)
