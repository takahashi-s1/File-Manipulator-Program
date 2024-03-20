# FileManipulatorProgram
コンピュータ・サイエンス学習サービス[Recursion](https://recursionist.io/)のアウトプットとして作成しました。

## プロジェクトの概要
簡単なファイル操作を行えるpythonスクリプトです。それぞれに応じたコマンドを入力することで、 ファイル内容を反転させたファイルの出力、 ファイルのコピー、 ファイル内容の繰り返し、 ファイル内検索が出来ます

## 実行方法

|  機能  |  コマンド  |
| --------- | --------- |
|reverse| python3 file_manipulator.py reverse input.txt output.txt|
|copy|python3 file_manipulator.py copy input.txt output.txt|
|duplicate-contents|python3 file_manipulator.py duplicate-contents input.txt output.txt num_dup|
|replace|python3 file_manipulator.py replace-string input.txt output.txt needle new_string|

## 学習
- コマンドライン引数の取得方法、操作
  - argparse
  - subparsers
- ファイル操作
  open(),read(),write(),close()

## 参照
- [実践python argparse](https://chaldene.net/argparse-parseargs)
- [公式ドキュメント](https://docs.python.org/ja/3/library/argparse.html#argparse.ArgumentTypeError)
- [コマンドライン引数](https://www.sejuku.net/blog/60106)
- [with](https://techplay.jp/column/1641)
- [raise](https://it-biz.online/python/raise/)
- [pythonノート](https://maku77.github.io/p/ybxfwev/)
