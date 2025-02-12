# create-note.ps1

# 引数の取得
$Category = $args[0]
$Filename = $args[1]

# 引数チェック
if (-not $Category -or -not $Filename) {
    Write-Host "Usage: .\create-note.ps1 [CATEGORY] [FILENAME]"
    exit 1
}

# 
$Template = ".github\template.md"       # テンプレートファイルのパス
$Date = Get-Date -Format "yyyyMMdd"     # 作成日
$MonthDir = Get-Date -Format "yyyyMM"   # 作成月
$TargetDir = "Articles\$MonthDir"       # 新規メモの保存先
$TargetFile = "$TargetDir\$Date`_$Category`_$Filename.md"   # 作成日付きのファイル名

# ディレクトリが存在しなければ作成
if (-not (Test-Path $TargetDir)) {
    New-Item -ItemType Directory -Path $TargetDir
}

# 同名ファイルが存在する場合はエラーメッセージを表示
if (Test-Path $TargetFile) {
    Write-Host "Error: $TargetFile already exists."
    exit 1
}

# GUID を生成 (id として使用)
$Guid = [guid]::NewGuid().ToString()

# メタデータを作成
$MetaData = @"
---
title: "$Category $Filename"
tags:
  - $Category
updated_at: ''
id: $Guid
---

"@

# テンプレートの内容を読み込み
$Content = Get-Content -Path $Template -Raw

# メタデータとテンプレートを結合
$FullContent = $MetaData + $Content

# UTF-8 (BOMなし) でファイルに書き込み
$FullContent | Set-Content -Path $TargetFile -Encoding UTF8

Write-Host "New note created: $TargetFile"
