---
title: "[Node.js] Windowsでアプリをデプロイ"
slug: deploy-nodejs-on-windows
date: 2016-04-04
categories:
- 開発
- Node.js
tags:
- Node.js
- Windows
keywords:
- Node.js Deploy
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/code/nodejs_svg.svg
metaAlignment: center
canonical: false
---
Linux系と違ってシステムユーザーじゃないとWindowsでNode.jsアプリをデプロイして、ログオフしたらアプリもダウンされてしまいます。
<a href="https://blogs.technet.microsoft.com/askds/2008/10/22/getting-a-cmd-prompt-as-system-in-windows-vista-and-windows-server-2008/" target="_blank"_ rel="noopener noreferrer">システムユーザー権限でCmd</a>を使用できますが、やり方が複雑すぎてめんどくさい。
<!--more-->

多分、一番簡単な方法はシステムサービスを使うことだと思います。
システムサービスにアプリサービスを登録できたらシステムユーザーがコントロールしてくれます。つまり、通常のユーザーがログオフしてもアプリが立ち上げっぱなしできます。

このノートで<a href="https://nssm.cc/" target="_blank"_ rel="noopener noreferrer">NSSM</a>を使用してNode.jsアプリをサービスとしてシステムサービスを登録し、
作業する.batファイルを投稿します。

## 1. システムサービスにアプリサービスを登録し開始する
{{< codeblock  "開始.bat" "bash" >}}
@echo off
@echo サービスをアンインストール...
nssm stop <SERVICE_NAME>
nssm remove <SERVICE_NAME>

@echo サービスをインストール...
nssm install <SERVICE_NAME> "node"

@echo 引数を設定...
nssm set <SERVICE_NAME> AppDirectory "path\to\app"
nssm set <SERVICE_NAME> AppParameters "index.js"
nssm set <SERVICE_NAME> AppEnvironmentExtra "NODE_ENV=production"
nssm set <SERVICE_NAME> AppStdout "path\to\logs\nssm_out.log"
nssm set <SERVICE_NAME> AppStderr "path\to\logs\nssm_err.log"

echo サービスを開始...
nssm start <SERVICE_NAME>

@timeout 10
{{< /codeblock >}}

## 2. サービスを停止し、システムサービスから削除する
{{< codeblock  "終了.bat" "bash" >}}
@echo off
@echo サービスをアンインストール...
nssm stop <SERVICE_NAME>
nssm remove <SERVICE_NAME>

@timeout 10
{{< /codeblock >}}

NSSMのコマンドラインの詳しくは<a href="https://nssm.cc/commands" target="_blank"_ rel="noopener noreferrer">HP</a>にご参考ください。
