---
title: 【Unity】 UniRxで購読するスレッドを指定する
tags:
  - Unity
  - UniRx
updated_at: ''
id: 523238d0-4834-4046-b140-0439d040b7c5
---
## 概要

UnityのAPIはメインスレッド上でしか呼び出せないという制限がある．（UnityAPIがスレッドセーフな実装ではないため）

また、Subscribeに渡した関数は基本的にIObserver.OnNextを実行したスレッド上で実行される．

## ObserveOnMainThread()

## SubscribeOn()

## 参考資料

- [qiita: ObserveOnとSubscribeOn](https://qiita.com/yaegaki/items/3189c799f6b80800c02d)
- [hatena: async/awaitやUniRxを使って非同期処理の後にメインスレッドで処理を行う](https://bluebirdofoz.hatenablog.com/entry/2020/12/03/232318)
- [MS: SynchronizationContextクラス](https://learn.microsoft.com/ja-jp/dotnet/api/system.threading.synchronizationcontext?view=net-9.0)

