---
title: Chain of Responsibility パターン
category: 設計
tags:
  - GoF
  - デザインパターン
---

**Chain of Responsibility（責任の連鎖）** は、 振る舞いに関するデザインパターンの一つで、 ハンドラーの連鎖に沿ってリクエストを渡すことができる． 各ハンドラーは、 リクエストを受け取ると、 リクエストを処理するか、 連鎖内の次のハンドラーに渡すかを決める．

<!-- more -->

## 構造

<img src="https://refactoring.guru/images/patterns/diagrams/chain-of-responsibility/structure-indexed-2x.png" width=350>

```puml
@startuml
' 要素
interface IHandler{
    + SetNext(h: IHandler)
    + Handle(rewuest)
}
abstract class BaseHandler{
    - next: IHandler
}
class ConcreateHandler{}

' 依存関係
IHandler <|.. BaseHandler
BaseHandler o--IHandler
BaseHandler <|-- ConcreateHandler
@enduml
```

- `IHandler`
  - すべての具象ハンドラに共通するインタフェース．
  - 通常はリクエストを処理するためのメソッドやのみを含む

- `BaseHandler`
  - 子要素を持たないツリー要素．

- `Concreate Handler`
  - リクエストを処理するための実コードをもつ．
  - 自身で処理出来ない場合は，連鎖に沿ってリクエストを次のハンドラへ委譲する．


## 適用例
`Chain of Responsibility`パターンは、フィルターやイベント・チェーンのようなオブジェクトの連鎖を対象に動作するコードを書く時に用いられる．


## 参考資料
- [Guru: Chain of Responsibility](https://refactoring.guru/ja/design-patterns/chain-of-responsibility)
- []()
- []()