# Reserve iframe
[![Change Vercel environment And Redeploy](https://img.shields.io/github/workflow/status/RTa-scp/reserveiframe/Change%20Vercel%20environment%20And%20Redeploy?label=Vercel&style=flat-square)](https://github.com/RTa-scp/reserveiframe/actions/workflows/vercel.yaml)
[![Expiration Checks](https://img.shields.io/github/workflow/status/RTa-scp/reserveiframe/Expiration%20Checks?label=Expiration%20Checks&style=flat-square)](https://github.com/RTa-scp/reserveiframe/actions/workflows/expirationcheck.yaml)
[![deploy](https://img.shields.io/github/workflow/status/RTa-scp/reserveiframe/deploy?label=Deploy&style=flat-square)](https://github.com/RTa-scp/reserveiframe/actions/workflows/pages.yaml)


This is a WebApp that generates an iframe for checking reserved translations for SCP-JP.
This WebApp consists of three repositories.
 - [RTa-scp/reserveiframe](https://github.com/RTa-scp/reserveiframe)
 - [RTa-technology/reserveapp](https://github.com/RTa-technology/reserveapp)
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
