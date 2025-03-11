---
title: PlayFabの認証
category: Unity
tags:
  - Unity
  - PlayFab
  - BaaS
---

`PlayFab`は

<!-- more -->

## プレイヤーのログイン

#### 匿名ログイン
匿名ログインは、プレイヤーがアカウント登録をせずにゲームをプレイできる方法．一時的なセッションを提供し、ユーザーが継続的にデータを保持できるようにする．ただし、デバイス変更時にデータが失われる可能性がある．

- [`LoginWithIOSDeviceID`][LoginWithIOSDeviceID]
- [`LoginWithAndroidDeviceID`][LoginWithAndroidDeviceID]
- [`LoginWithCustomID`][LoginWithCustomID]

これらはデバイスを一意に識別することができるが、匿名であるためプレイヤーに関して回復可能な情報はない．よって，プレイヤーがデバイスを紛失または破壊した場合、アカウントは失われることになる．

> Tips
> これらの方法はプレイヤーに何の操作も要求しないため，障壁が低いというメリットがある．実際，プレイヤーによっては，メールアドレスやID情報を尋ねると，ゲームを断念することがある．したがって，最初は匿名ログインで開始して，ログイン完了後に回復可能なログイン資格情報を追加できる仕組みが好ましい．

#### 回復可能なログイン
プレイヤーが異なるデバイス間でデータを引き継ぐために使用するログイン方法．

**純粋なPlayFabオプション**

- [`LoginWithPlayFab`][LoginWithPlayFab]
- [`LoginWithEmailAddress`][LoginWithEmailAddress]

**サードパーティのAPIオプション**
- [`LoginWithKongregate`][LoginWithKongregate]
- [`LoginWithSteam`]
- [`LoginWithTwitch`]
- [`LoginWithGameCenter`] (iOSのみ．セキュリティで保護された認証が必要な場合)

**サードパーティのSDKオプション**

- `LoginwithFacebook`
- `LoginWithGoogleAccount`


## ログイン

<img src="https://learn.microsoft.com/ja-jp/gaming/playfab/features/authentication/media/tutorials/playfab-anonymous-login-and-recoverable-login.png" width=600>


## 参考資料
- [MS: ログインの基本とベストプラクティス](https://learn.microsoft.com/ja-jp/gaming/playfab/features/authentication/login/login-basics-best-practices)


[LoginWithIOSDeviceID]: https://learn.microsoft.com/ja-jp/rest/api/playfab/client/authentication/login-with-ios-device-id?view=playfab-rest
[LoginWithAndroidDeviceID]: https://learn.microsoft.com/ja-jp/rest/api/playfab/client/authentication/login-with-android-device-id?view=playfab-rest
[LoginWithCustomID]: https://learn.microsoft.com/ja-jp/rest/api/playfab/client/authentication/login-with-custom-id?view=playfab-rest

[LoginWithPlayFab]: https://learn.microsoft.com/ja-jp/rest/api/playfab/client/authentication/login-with-playfab?view=playfab-rest
[LoginWithEmailAddress]: https://learn.microsoft.com/ja-jp/rest/api/playfab/client/authentication/login-with-email-address?view=playfab-rest

[LoginWithKongregate]: https://learn.microsoft.com/ja-jp/rest/api/playfab/client/authentication/login-with-kongregate?view=playfab-rest
[LoginWithSteam]: https://learn.microsoft.com/ja-jp/rest/api/playfab/client/authentication/login-with-steam?view=playfab-rest
[LoginWithTwitch]: https://learn.microsoft.com/ja-jp/rest/api/playfab/client/authentication/login-with-twitch?view=playfab-rest
[LoginWithGameCenter]: https://learn.microsoft.com/ja-jp/rest/api/playfab/client/authentication/login-with-game-center?view=playfab-rest