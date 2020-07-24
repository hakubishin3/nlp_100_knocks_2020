"""
06. 集合
“paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""


def n_gram(seq: list, n: int) -> list:
    return ["".join(seq[idx:idx+n]) for idx in range(len(seq))]


text_x = "paraparaparadise"
text_y = "paragraph"
X = n_gram(list(text_x), 2)
Y = n_gram(list(text_y), 2)

print("和集合:", set(X) | set(Y))
print("積集合:", set(X) & set(Y))
print("差集合:", set(X) - set(Y))
print("se:", "se" in (set(X) | set(Y)))
