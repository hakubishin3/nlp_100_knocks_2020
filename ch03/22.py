"""
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
"""
import pandas as pd
import re


df = pd.read_json("./data/jawiki-country.json", lines=True)
uk_text = df.query("title=='イギリス'")["text"].values[0]

answer = [obj.replace("[[Category:", "").replace("]]", "").split("|")[0] for obj in re.findall(r"\[\[Category:.+\]\]", uk_text)]
print(answer)
