"""
28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
"""
import pandas as pd
import re

"""
https://github.com/upura/nlp100v2020/blob/master/ch03/ans28.py
"""
def remove_mk(v):
    r1 = re.compile("'+")
    r2 = re.compile('\[\[(.+\||)(.+?)\]\]')
    r3 = re.compile('\{\{(.+\||)(.+?)\}\}')
    r4 = re.compile('<\s*?/*?\s*?br\s*?/*?\s*>')
    v = r1.sub('', v)
    v = r2.sub(r'\2', v)
    v = r3.sub(r'\2', v)
    v = r4.sub('', v)
    return v


df = pd.read_json("./data/jawiki-country.json", lines=True)
uk_text = df.query("title=='イギリス'")["text"].values[0]

answer = {}
for sub in re.findall(r'\|(.+?)\s=\s*(.+)', uk_text):
    answer[sub[0]] = sub[1]
answer = {k: re.sub(r"'{2,}", "", v) for k, v in answer.items()}
answer = {k: re.sub(r"\[\[(.+\||)(.+?)\]\]", "\2", v) for k, v in answer.items()}
answer = {k: remove_mk(v) for k, v in answer.items()}
print(answer)

