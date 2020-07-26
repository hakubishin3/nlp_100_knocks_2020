"""
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ.
"""
import pandas as pd
import re


df = pd.read_json("./data/jawiki-country.json", lines=True)
uk_text = df.query("title=='イギリス'")["text"].values[0]

answer = [(obj.replace("=", ""), obj.count("=")//2 - 1) for obj in re.findall(r"={2,}.+={2,}", uk_text)]
print(answer)
