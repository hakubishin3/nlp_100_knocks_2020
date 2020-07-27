"""
29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
"""
import pandas as pd
import requests
import re

"""
https://github.com/upura/nlp100v2020/blob/master/ch03/ans29.py
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


def get_url(dc):
    url_file = dc['国旗画像'].replace(' ', '_')
    url = 'https://commons.wikimedia.org/w/api.php?action=query&titles=File:' + url_file + '&prop=imageinfo&iiprop=url&format=json'
    data = requests.get(url)
    return re.search(r'"url":"(.+?)"', data.text).group(1)


df = pd.read_json("./data/jawiki-country.json", lines=True)
uk_text = df.query("title=='イギリス'")["text"].values[0]

answer = {}
for sub in re.findall(r'\|(.+?)\s=\s*(.+)', uk_text):
    answer[sub[0]] = sub[1]
answer = {k: re.sub(r"'{2,}", "", v) for k, v in answer.items()}
answer = {k: re.sub(r"\[\[(.+\||)(.+?)\]\]", "\2", v) for k, v in answer.items()}
answer = {k: remove_mk(v) for k, v in answer.items()}
print(get_url(answer))

