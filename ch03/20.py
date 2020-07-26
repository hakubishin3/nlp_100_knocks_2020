"""
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""
import pandas as pd


df = pd.read_json("./data/jawiki-country.json", lines=True)
uk_text = df.query("title=='イギリス'")["text"]
print(uk_text)
