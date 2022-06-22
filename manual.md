# 初めに
このツールは未翻訳の翻訳されたSCP-JPページにて，だれがいつからいつまで翻訳期間かを生成するものです．

# システム構成
![](/reservebot.jpg)

# 使い方
1. 翻訳予約フォームにて追記したときにGASからreserveappにget reqを贈ります．
2. reserveappでcreate/update/deleteの処理を行う(Github)
3. Github Pagesでhtmlを生成する
4. _404にてiframeで表示する

# 注意
## `GITHUB_ACCESS_TOKEN`
Vercelの環境変数に置いてある`GITHUB_ACCESS_TOKEN` はGithub Apps(ReserveBot)のAccess Tokenです．  
Access Tokenの有効期限は40~50分です．その為，Github Actionsで30分おきに更新をかけています．  
もし，`HTTP_401_UNAUTHORIZED`が出た場合は，Github Actions [[change] Change Vercel environment And Redeploy
](https://github.com/RTa-scp/reserveiframe/actions/workflows/vercel.yaml)を手動実行して`GITHUB_ACCESS_TOKEN`を更新してください．


## Githubの環境変数
```
VERCEL_PROJECT_ID = ""
VERCEL_ENV_ID = "" # not show name, hash ID
VERCEL_TOKEN = ""
APP_ID = ""
REPO_ID = "" # app repo id
REPO_NAME = "" # app repo name
INSTALLATION_ID = ""
PRIVATE_KEY = "-----BEGIN RSA PRIVATE KEY-----\n.......\n-----END RSA PRIVATE KEY-----"
ACCESS_TOKEN_REPO = ""
```
