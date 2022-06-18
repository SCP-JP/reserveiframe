import requests
import sys
import os
from dotenv import load_dotenv
import traceback

def main():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    url = os.getenv('APISERVER_DOMAIN')+'/health/reserve'
    r = requests.get(url)
    if r.status_code != 200:
        print("::error:: Not Working API Server")
        sys.exit(1)
    print(r.text)
    sys.exit(0)

if __name__ == '__main__':
    main()
