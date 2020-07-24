"""
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ.
ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文（例えば”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）を与え，その実行結果を確認せよ．
"""
import random


def reorder(word):
    start_char = word[0]
    end_char = word[-1]
    shuffle_char = random.sample(word[1:-1], k=len(word[1:-1]))
    return "".join([start_char] + shuffle_char + [end_char])


def check_typoglycemia(text: str) -> str:
    word_list = text.split()
    result = [reorder(w) if len(w) > 4 else w for w in word_list]
    return " ".join(result)


text = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
answer = check_typoglycemia(text)
print(answer)
