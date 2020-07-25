# 17. １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはcut, sort, uniqコマンドを用いよ．


cut -d $'\t' -f 1 ./data/popular-names.txt | sort | uniq >> answer17.txt
