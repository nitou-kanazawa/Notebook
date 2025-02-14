---
title: "【Win32】windows NtCreateFile関数"
tags:
  - WindowsAPI
updated_at: ''
id: 3c4a7d99-cb3b-4487-bb2c-61ec581f605a
---

## 概要
C#で`SMBファイル共有`関連のライブラリを利用する際に、`CreateFile()`でハンドルを取得する必要があった．このとき、


## Win32API

> Microsoft Windowsのシステムコール用APIのこと。特に32ビットプロセッサで動作するWindows 95以降やWindows NTで利用できるものはWin32 APIと呼ばれる。
64ビットプロセッサ向けのWin64 APIも含める場合は「Windows API」という包括的な名称が正確だが、慣習的にWin32と言えばWin64も含んでいることがある

- [wiki: Windows API](https://ja.wikipedia.org/wiki/Windows_API)
- [qiita: C# Win32API完全入門](https://qiita.com/nekotadon/items/f376d17de85dfb84fbd5)
- [qiita: 今更聞けない(かもしれない)Win32API概要](https://qiita.com/kamikawa_m/items/061dc6d7fbcf95cf7ed0)

C#から呼び出す場合は`P/Invoke`を使用するか、公式のC#ライブラリを用いる．

[nuget: Microsoft.Windows.CsWin32](https://www.nuget.org/packages/Microsoft.Windows.CsWin32)

## CreateFile関数

- NTCreateFile


##

## 参考資料

- []()
- []()
- []()
