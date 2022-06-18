# readmeのbadgeのlabelに実行時間を記載する．

import os 
import datetime
import re
import sys
import pytz

def get_time():
    now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    return now.strftime("%Y-%m-%d %H:%M")


def get_date():
    now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    return now.strftime("%Y-%m-%d")

def main(type):
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    with open(readme_path, 'r') as f:
        readme = f.read()
    if type == 'vercel':
        pattern = r'label\=Vercel\%20run:\%20([0-9-]+)\%20([0-9:]+)\&style\=flat-square'
    elif type == 'expiration':
        pattern = r'label\=Expiration\%20Checks\%20date:\%20([0-9-]+)\&style\=flat-square'
    elif type == 'deploy':
        pattern = r'label\=Deploy\%20run:\%20([0-9-]+)\%20([0-9:]+)\&style\=flat-square'
    elif type == 'survive':
        pattern = r'label\=Survive\%20run:\%20([0-9-]+)\%20([0-9:]+)\&style\=flat-square'
    match = re.search(pattern, readme)
    if match:
        now = get_time().replace(' ', '%20')
        date = get_date()
        if type == 'vercel':
            readme = re.sub(pattern, 'label=Vercel%20run:%20' + now + '&style=flat-square', readme)
        elif type == 'expiration':
            readme = re.sub(pattern, 'label=Expiration%20Checks%20date:%20' + date + '&style=flat-square', readme)
        elif type == 'deploy':
            readme = re.sub(pattern, 'label=Deploy%20run:%20' + now + '&style=flat-square', readme)
        elif type == 'survive':
            readme = re.sub(pattern, 'label=Survive%20run:%20' + now + '&style=flat-square', readme)
    with open(readme_path, 'w') as f:
        f.write(readme)

if __name__ == '__main__':
    args = sys.argv
    main(args[1])