---
title: IEnumerable<T>とIEnumrator<T>
category: C#
tags:
  - C#
  - LINQ
---

[`IEnumerable<T>`][IEnumerable<T>]，はジェネリックコレクション（System.Generic.Collection）を反復

<!-- more -->



##  IEnumrator<T>

```cs
public interface IEnumerator<out T> {
    bool MoveNext();
    T Current { get; }
}
```

## 

```cs
public interface IEnumerable<out T> : System.Collections.IEnumerable {

}
```

互換性を維持するために`IEnumerable<T>`は`IEnumerable`を実装するが，現在のC#で非ジェネリックのコレクションは基本的にない．


<!-- リンク -->
[IEnumerable<T>]: https://learn.microsoft.com/ja-jp/dotnet/api/system.collections.generic.ienumerable-1?view=net-8.0