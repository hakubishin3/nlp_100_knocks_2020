# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．


sed -e "s/[[:cntrl:]]/ /g" ./data/popular-names.txt >> answer11.txt
