# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．


cut -d $'\t' -f 1 ./data/popular-names.txt | sort | uniq -c | sort -r -k 2 -t $'\t' >> answer19.txt
