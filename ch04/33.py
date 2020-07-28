"""
33. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
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

no_idx = [i for i, morpheme in enumerate(morphemes) if morpheme["surface"] == "の"]
answer = []
for idx in no_idx:
    if (idx -1 < 0) or (idx + 1 > len(morphemes)):
        continue
    elif morphemes[idx-1]["pos"] == "名詞" and morphemes[idx+1]["pos"] == "名詞":
        answer.append(morphemes[idx-1]["surface"] + morphemes[idx]["surface"] + morphemes[idx+1]["surface"])
print(answer)
