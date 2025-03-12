---
title: PlayFabでプレイヤーデータを管理する
category: Unity
tags:
  - Unity
  - PlayFab
---

`PlayFab`でのユーザ認証には「匿名ログイン」と「復旧可能ログイン」の2種類がある．

<!-- more -->


## プレイヤーデータ（タイトル）

#### 各種データの違い

|データ| クライアント| サーバー| 更新メソッド| 取得メソッド| 
|------|-------------|---------|-------------|-------------|
|プレイヤーデータ | CRUD | CRUD | UpdateUserData | GetUserData |
|読み取り専用データ| R | CRUD | UpdateUserReadOnlyData | GetUserReadOnlyData|
|内部データ| - | CRUD | UpdateUserInternalData | GetUserInternalData |


#### アクセス許可

`public`の場合，他プレイヤーのクライアントコードからデータアクセスが可能となる．必要なければ基本的に`private`にすべき．


## データの更新

データ更新は`UpdateUsarData`を使用する．

データを更新する場合は，引数`Data`に`Dictionary<string, string>`形式でデータを渡す．指定したキーが未登録の場合は新規，登録済みの場合は更新としてサーバー上に登録される．
データを削除する場合は，引数`KeysToRemove`に削除するキーをList形式で渡す．

```cs
var request = new UpdateUserDataRequest{
  // 更新するデータ
  Data = new Dictionary<string, string>{
    {"Name", "neko"},
    {"Exp", "1000"}
  }
  // 削除するデータ
  KeysToRemove = new List<string> {"Attack"}
}

PlayFabClientAPI.UpdateUserData(request, onSuccess, onError);
```

## 参考資料
- []()
- []()