"""
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
"""


def n_gram(seq: list, n: int) -> list:
    return ["".join(seq[idx:idx+n]) for idx in range(len(seq))]


text = "I am an NLPer"
char_list = list(text.replace(" ", ""))
word_list = text.split()
answer_char_bi = n_gram(char_list, 2)
answer_word_bi = n_gram(word_list, 2)
print(answer_char_bi)
print(answer_word_bi)
