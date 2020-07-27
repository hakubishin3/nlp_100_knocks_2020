"""
27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ.
"""
import pandas as pd
import re


df = pd.read_json("./data/jawiki-country.json", lines=True)
uk_text = df.query("title=='イギリス'")["text"].values[0]

answer = {}
for sub in re.findall(r'\|(.+?)\s=\s*(.+)', uk_text):
    answer[sub[0]] = sub[1]
answer = {k: re.sub(r"'{2,}", "", v) for k, v in answer.items()}
answer = {k: re.sub(r"\[\[(.+\||)(.+?)\]\]", "\2", v) for k, v in answer.items()}
print(answer)
