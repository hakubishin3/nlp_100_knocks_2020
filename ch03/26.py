"""
26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ.
"""
import pandas as pd
import re


df = pd.read_json("./data/jawiki-country.json", lines=True)
uk_text = df.query("title=='イギリス'")["text"].values[0]

answer = {}
for sub in re.findall(r'\|(.+?)\s=\s*(.+)', uk_text):
    answer[sub[0]] = sub[1]
answer = {k: re.sub(r"'{2,}", "", v) for k, v in answer.items()}
print(answer)
