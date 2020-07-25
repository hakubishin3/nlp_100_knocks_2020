# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．


n=`cat ./data/popular-names.txt | wc -l`
ln=`expr $n / $1`
split -l $ln ./data/popular-names.txt answer16_
