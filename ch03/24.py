"""
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
"""
import pandas as pd
import re


df = pd.read_json("./data/jawiki-country.json", lines=True)
uk_text = df.query("title=='イギリス'")["text"].values[0]

for sub in re.findall(r'\[\[(ファイル|File):([^|]+?)(\|.*?)+\]\]', uk_text):
    print(sub[1])
