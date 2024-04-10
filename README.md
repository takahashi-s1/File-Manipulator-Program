# FileManipulatorProgram
## 概要
簡単なファイル操作を行えるpythonスクリプトです。  
各コマンドを入力することで、 「ファイル内容を反転させたファイルの出力」「ファイルのコピー」「ファイル内容の繰り返し」「ファイル内検索」ができます。
## 背景
CS知識を学習するために作成しました。  
   
参考：コンピュータ・サイエンス学習サービス[Recursion](https://recursionist.io/)

## 実行方法
CLI（コマンドライン）を通して以下のコマンドを入力する事でそれぞれの機能を使用する事ができます。

inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成
```
python3 file_manipulator.py reverse input.txt output.txt
```

inputpath にあるファイルのコピーを作成し、outputpath として保存する
```
python3 file_manipulator.py copy input.txt output.txt
```

inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製
```
python3 file_manipulator.py duplicate-contents input.txt output.txt num_dup
```

inputpath' にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換え
```
python3 file_manipulator.py replace-string input.txt output.txt needle new_string
```


以下は機能を表にまとめたものです。

|  機能  |  コマンド  |
| --------- | --------- |
|reverse| python3 file_manipulator.py reverse input.txt output.txt|
|copy|python3 file_manipulator.py copy input.txt output.txt|
|duplicate-contents|python3 file_manipulator.py duplicate-contents input.txt output.txt num_dup|
|replace|python3 file_manipulator.py replace-string input.txt output.txt needle new_string|

## 学習
- コマンドライン引数の取得
  - argparse
  - subparsers
- ファイル操作
  - open(),read(),write(),close()
  - modeパラメータ

## 参照
- [実践python argparse](https://chaldene.net/argparse-parseargs)
- [公式ドキュメント](https://docs.python.org/ja/3/library/argparse.html#argparse.ArgumentTypeError)
- [コマンドライン引数](https://www.sejuku.net/blog/60106)
- [with](https://techplay.jp/column/1641)
- [raise](https://it-biz.online/python/raise/)
- [pythonノート](https://maku77.github.io/p/ybxfwev/)
