"""
32. 動詞の原形
動詞の原形をすべて抽出せよ．
"""


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

answer = [morpheme["base"] for morpheme in morphemes if morpheme["pos"] == "動詞"]
print(answer)
