---
title: Blazorとは
category: C#
tags:
  - C#
updated_at: ''
id: b87da14e-4cd7-4cb3-b19c-d23efe8686e1
---

`Blazor（ブレイザー）`は，C#とRazorを使ってWebアプリケーションを開発できるフレームワーク．Microsoftが開発しており，.NET技術を使ってフロントエンドの開発ができるのが特徴である．


## Blazorの主な特徴

1. **C#でフロントエンド開発が可能**  
   - JavaScriptの代わりにC#でUIを操作できる．
   - .NETのエコシステム（ライブラリ，DI，非同期処理など）が活用できる．

2. **コンポーネントベースの開発**  
   - `React`や`Vue.js`のように、**UIをコンポーネント化**して開発できる
   - `Razor Component` という仕組みで、HTML + C#を組み合わせたコンポーネントを作成．

3. **2つのホスティングモデル**
   - `Blazor Server`（サーバーサイドレンダリング）
   - `Blazor WebAssembly（WASM）`（クライアントサイドレンダリング）


#### **Blazorのホスティングモデル**
| モデル | 特徴 |
|--------|------|
| **Blazor Server** | - UI処理はサーバー側で行い、SignalRでクライアントと通信．<br>- 初回読み込みが速いが、ネットワーク接続が必須．|
| **Blazor WebAssembly** | - WebAssembly上でC#コードを実行．<br>- クライアントサイドで動作するのでオフラインでも動くが、初回ロードが重い． |







##

## 参考資料

- [zenn: .NET8でのBlazorを整理整頓して理解しよう](https://zenn.dev/microsoft/articles/blazor-dotnet8-all)
- []()
- []()


### **Blazorの基本コード例**
#### **シンプルなカウンターコンポーネント**
```razor
@page "/counter"

<h3>カウンター</h3>
<p>現在のカウント: @count</p>
<button @onclick="Increment">増やす</button>

@code {
    private int count = 0;

    private void Increment()
    {
        count++;
    }
}
```
- `@page "/counter"` → ルートURL `/counter` でアクセス可能
- `@count` → 変数の値をHTMLに埋め込み
- `@onclick="Increment"` → ボタンがクリックされたら `Increment` メソッドを実行
- `@code { }` → C#コードを記述

---

### **Blazorのメリット**
✅ **C#だけでフルスタック開発** → フロントエンドとバックエンドの言語を統一  
✅ **JavaScript不要**（JSとの相互運用も可能）  
✅ **.NETの豊富なライブラリが使える**  
✅ **コンポーネントベースの開発ができる**  

### **Blazorのデメリット**
❌ **WebAssembly版（WASM）は初回ロードが遅い**  
❌ **ブラウザの互換性に注意（特にBlazor WebAssembly）**  
❌ **JavaScriptエコシステム（npm, React, Vueなど）と比べるとまだ発展途上**  

---

### **Blazorはどんな場面で使うべき？**
- **C#/.NETの知識があり、フロントエンドもC#で書きたい**
- **社内ツールや管理画面など、.NET環境のWebアプリを作りたい**
- **JavaScriptをあまり書きたくないが、Webアプリを作りたい**

---

### **Blazorを試してみるには？**
Blazorプロジェクトの作成:
```sh
dotnet new blazorwasm -o MyBlazorApp
cd MyBlazorApp
dotnet run
```
`http://localhost:5000` にアクセスすれば動作確認できます。

---

### **まとめ**
- **BlazorはC#でWebアプリが作れるフレームワーク**
- **Blazor Server（サーバー処理）と Blazor WebAssembly（クライアント処理）**
- **コンポーネントベースで開発可能**
- **.NET開発者には便利だが、JavaScriptエコシステムと比較するとまだ発展途上**

C#メインで開発しているなら、試してみる価値アリです！