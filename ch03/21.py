"""
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
"""
import pandas as pd
import re


df = pd.read_json("./data/jawiki-country.json", lines=True)
uk_text = df.query("title=='イギリス'")["text"].values[0]
uk_text = uk_text.split("\n")

answer = [i for i, obj in enumerate(uk_text) if re.search(r"\[Category:", obj)]
print(answer)
