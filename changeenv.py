from re import I
import requests
import json
import os
from dotenv import load_dotenv
import githubapps
from github import Github
import sys

def get_env(env_value):
    # Vercelの環境変数を取得
    # env_name: 環境変数名
    # env_value: 環境変数の値

    url = 'https://api.vercel.com/v9/projects/{idOrName}/env/'.format(
        idOrName=os.getenv('VERCEL_PROJECT_ID'))
    print(url)
    headers = {'Authorization': 'Bearer ' + os.getenv('VERCEL_TOKEN')}
    response = requests.get(url, headers=headers)
    return response.json()


def change_env(env_value):
    # Vercelの環境変数を書き換える
    # env_name: 環境変数名
    # env_value: 環境変数の値
    # return: 書き換え結果

    url = 'https://api.vercel.com/v9/projects/{idOrName}/env/{id}'.format(
        idOrName=os.getenv('VERCEL_PROJECT_ID'), id=os.getenv('VERCEL_ENV_ID'))
    headers = {'Authorization': 'Bearer ' + os.getenv('VERCEL_TOKEN')}
    data = {
        'value': env_value,
    }
    response = requests.patch(url, headers=headers, json=data)
    if response.status_code == 200:
        return 'change_env: Success'
    else:
        print("::error:: Not Changing Environment")
        sys.exit(1)


def redeploy(env_value, commit_sha):
    # vercelを再deployする
    # return: 再deploy結果
    url = 'https://api.vercel.com/v13/deployments'
    headers = {'Authorization': 'Bearer ' + os.getenv('VERCEL_TOKEN')}
    data = {
        "name": "reserveapp",
        "gitSource": {
            "ref": "main",
            "org": "RTa-technology",
            "repo": os.getenv('REPO_NAME'),
            "repoId": os.getenv('REPO_ID'),
            "sha": commit_sha,
            "type": "github",
            "prId": "null"
        },
        "target": "production"
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return 'redeploy: Success'
    else:
        print("::error:: Not Redeploying")
        sys.exit(1)

def main():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    if os.getenv('APP_ID') is not None:
        private_key = os.getenv('PRIVATE_KEY').replace("\\n", '\n').encode()
        app_id = os.getenv('APP_ID')
        installation_id = os.getenv('INSTALLATION_ID')
        auth = githubapps.RequestsAuth(app_id, installation_id, private_key)
        access_token = auth.get_access_token()
        # print(access_token)
        print(change_env(access_token))
        g = Github(os.getenv('ACCESS_TOKEN_REPO'))
        branch = g.get_repo("RTa-technology/{}".format(os.getenv('REPO_NAME'))).get_branch("main")
        commit_sha = branch.commit.sha
        print(redeploy(access_token, commit_sha))

if __name__ == "__main__":
    main()
