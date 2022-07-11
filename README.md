# Reserve iframe
## Deploy and Expiration Checks
[![deploy](https://img.shields.io/github/workflow/status/SCP-JP/reserveiframe/%5Bdocs%5D%20deploy/reserve?label=Deploy%20run:%202022-07-07%2010:03&style=flat-square)](https://github.com/SCP-JP/reserveiframe/actions/workflows/pages.yaml)
[![Expiration Checks](https://img.shields.io/github/workflow/status/SCP-JP/reserveiframe/%5Bcheck%5D%20Expiration%20Checks?label=Expiration%20Checks%20date:%202022-07-11&style=flat-square)](https://github.com/SCP-JP/reserveiframe/actions/workflows/expirationcheck.yaml)

## Vercel surveillance
[![Change Vercel environment And Redeploy](https://img.shields.io/github/workflow/status/SCP-JP/reserveiframe/%5Bchange%5D%20Change%20Vercel%20environment%20And%20Redeploy?label=Vercel%20run:%202022-07-11%2013:56&style=flat-square)](https://github.com/SCP-JP/reserveiframe/actions/workflows/vercel.yaml)
[![surveillance](https://img.shields.io/github/workflow/status/SCP-JP/reserveiframe/%5Bcheck%5D%20Vercel%20surveillance?label=Survive%20run:%202022-07-11%2014:20&style=flat-square)](https://github.com/SCP-JP/reserveiframe/actions/workflows/surveillance.yaml)


This is a WebApp that generates an iframe for checking reserved translations for SCP-JP.
This WebApp consists of three repositories.
 - [SCP-JP/reserveiframe](https://github.com/SCP-JP/reserveiframe)
 - [SCP-JP/reserveapp](https://github.com/SCP-JP/reserveapp)
 - [RTa-technology/githubapps.py](https://github.com/RTa-technology/githubapps.py)
When a get request is made to [zzzzzzz](#), files in this repository are edited/deleted.
Github Pages generates html at [xxx/reserve/_default/yyyyyy](#) after seeing the update.
# Develop
`.env` and Github Repo Secret
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
Vercel Environments
```
GITHUB_ACCESS_TOKEN = ""
```
