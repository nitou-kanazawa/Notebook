---
title: UnityでPlayFabを利用する
category: Unity
tags:
  - Unity
  - PlayFab
  - BaaS
---

[`PlayFab`](https://azure.microsoft.com/ja-jp/products/playfab)は，ゲーム開発に特化された`BasS (Backend as a Service)`の1つ．

<!-- more -->

#### PlayFabの機能

`PlayFab`は様々な機能を備えており，ドキュメントには`Multiplayer Services`，`LiveOps Services`，`Data & Analytices`のカテゴリに分けて以下のように示されている．

- Multiplayer Services
  - クロスネットワークのIDとデータ
  - マルチプレイヤーサーバー
  - チャット
  - ランキングと統計

- LiveOps Services
  - エンゲージメントとリテンション
  - コンテンツ管理
  - A/Bテスト
  - 収益化
  - 自動化

- Data & Analytics
  - リアルタイム分析
  - データ管理
  - コンプライアンス
  - SDK
  - サポート
  

## PlyaFabを始める

Unityで利用するために，サーバー／クライアント側でそれぞれ以下の対応が必要である．
1. Unityへ`Unity3d PlayFab SDK` を導入
2. `ゲームマネージャー`でタイトルを作成

## 1. Unityでの作業

#### PlayFab SDK 
`Unity3d PlayFab SDK` には、モデル、メソッド、Web 要求を送受信するための HTTP ラッパー、JSON シリアル化など、PlayFab API にアクセスするために必要なすべてのものが用意されている．

[Unity PlayFab SDK GitHub リポジトリ](https://github.com/PlayFab/UnitySDK)

このSDKはマイクロソフトの`SDKGenerator`によって自動生成されている．最新のAPIを反映するために通常2週間ごとにビルドされている．

#### SDKのインストール


[SDKパッケージ](https://aka.ms/playfabunitysdkdownload)


## 2. ゲームマネージャーでの作業

#### PlayFabアカウント

Microsoftアカウントを使用してサインインする必要がある．

<img src="https://learn.microsoft.com/ja-jp/gaming/playfab/gamemanager/media/quickstart/create-account.png" alt="アカウントの作成" width =400>

> [!CAUTION]
> PlayFab固有アカウントを用いたサインインも可能だが，こちらは2025年4月30日にゲームマネージャーでのサポートが廃止されるため、Microsoftアカウントを利用する必要がある．

#### ゲームの作成

<img src="https://learn.microsoft.com/ja-jp/gaming/playfab/gamemanager/media/quickstart/create-first-game.png" alt="ゲームの作成" width =400>

#### スタジオとタイトル

`PlayFab`には「スタジオ」と「タイトル」という重要な概念がある．
  - タイトル：１つのゲーム
  - スタジオ：複数のゲームが入る箱


<img src="https://learn.microsoft.com/ja-jp/gaming/playfab/gamemanager/media/quickstart/my-studios-titles.png" alt="スタジオとタイトル" width="600">


## 参考資料

- [MS: PlayFabとは？](https://learn.microsoft.com/ja-jp/gaming/playfab/what-is-playfab)
- [MS: UnityのC#用のPlayFabクライアントライブラリ](https://learn.microsoft.com/ja-jp/gaming/playfab/sdks/unity3d/quickstart)
- [zenn: ゲーム開発が10倍ラクになる「PlayFab」の始め方](https://zenn.dev/nekojoker/articles/38f1654ee254f482dfce)