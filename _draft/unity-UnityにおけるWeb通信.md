---
title: UnityにおけるWeb通信
category: Unity
tags:
  - Unity
  - Http
  - WebAPI
---


## Unityにおける通信API

1. `WWW` (古くからUnityで提供されているAPI)
2. `UnityWebRequest` (Unity5.4系より正式提供されているAPI)
3. `HttpWebRequest` (C#標準で提供されているAPI)
4. ネイティブプラグインを利用した通信処理の独自実装


#### WWW
`WWW`は古くからUnityで提供されているAPIで，コルーチンとの親和性や記述の少なさと言った点で他のAPIより優れている．GET，POSTを行える．

[ドキュメント](https://docs.unity3d.com/ja/2023.2/ScriptReference/WWW.html)

```cs
IEnumerator Download(string url, string path){
    WWW www = new WWW(url);
    yield return www;
    File.WriteAllBytes(path, www.bytes);    // need to handle error
}
```


#### UnityWebRequest
`UnityWebReuqest`はUnity 5.2より実験的に導入され，5.4より正式機能となった，`WWW`に代わる次世代通信API．

```cs
IEnumerator Download(string url, string path) {
    using (UnityWebRequest request = UnityWebRequest.Get(url)) {
        yield return request.Send();
        File.WriteAllBytes(path, request.downloadHandler.data); // need to handle error
    }
}
```


#### HttpWebRequest


#### ネイティブ実装




## 参考資料

- [CyberAgent: Unityにおける通信APIを色々試して罠を踏んだ話](https://developers.cyberagent.co.jp/blog/archives/6649/)
- []()
- [qiita: 初心者が送る UnityでAPI通信講座](https://qiita.com/pchan52/items/feca16ea98289ec31c65)
- [qiita: UnityWebRequestを（Taskクラスを使わずに）Awaitableにする](https://qiita.com/k7a/items/80984aaf4abae180816c)
- [qiita: UnityでHTTPに接続する](https://qiita.com/ponchan/items/65aeb43e8fea8da0bcac)
- []()
- []()
