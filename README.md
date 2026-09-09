# 歩留まりとチップ単価をPythonで計算する｜1枚のウェハから何個取れるか

半導体のコストを決める「ウェハから取れるチップ数」と「歩留まり」を、Pythonで計算。ダイサイズを変えるとコストがどう動くのか、なぜ大きなチップは割高になるのかを、Murphyの歩留まりモデルで確かめます。

> 📖 このコードの詳しい解説（理論・図解つき）は元記事をどうぞ:
> **[歩留まりとチップ単価をPythonで計算する｜1枚のウェハから何個取れるか](https://semiconductor.yurufuwa.work/learn/yield-cost-python)** — ゆるふわ半導体

## セットアップ

```bash
pip install -r requirements.txt
```

## 実行方法

```bash
python yield-cost-python.py
```

## これは何？

[ゆるふわ半導体](https://semiconductor.yurufuwa.work) はやさしい技術解説サイト「ゆるふわ」シリーズの一つです。このリポジトリは記事内で解説しているコードをそのまま動かせる形にまとめた、記事の副教材（コンパニオンリポジトリ）です。

## License

MIT
