# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．


cut -d $'\t' -f 1 ./data/popular-names.txt >> col1.txt
cut -d $'\t' -f 2 ./data/popular-names.txt >> col2.txt
