---
title: 「A Tour of Go」でGo言語に入門する
category: Go
tags:
  - Go
---


[A Tour of Go]は


## Go言語について


```go
pacage main

import{
  "fmt"
  "math/rand"
}

func main(){
  fmt.PrintIn("My favorite number is", rand.Intn(10))
}
```

## GO言語の特徴

#### オブジェクト志向ではない
`Go`は`C`などと同様に手続き型言語である．よって，クラスが存在せず，構造体で独自型を定義することになる．

#### 関数は複数の値を返す


#### 例外処理がない
`Go`では「関数の呼び出し元がエラー処理をすべき」という考えがあり，




## Basics

#### Packages


#### Exported names
Goではアクセス修飾が変数名や関数名の最初の文字が大文字or小文字によって決まる．

```go
// publicなメソッド
func Foo(){ }

// privateなメソッド
func foo(){ }
```

#### Variables

#### 

#### 

#### 

## 


## 


## 
