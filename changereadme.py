# readmeのbadgeのlabelに実行時間を記載する．

import os 
import datetime
import re
from turtle import pen
import pytz

def get_time():
    now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    return now.strftime("%Y-%m-%d %H:%M")

def main():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    with open(readme_path, 'r') as f:
        readme = f.read()
    # label=Vercel%20YYYY-MM-DD%20HH:MM&style=flat-square
    pattern = r'label\=Vercel\%20run:\%20([0-9-]+)\%20([0-9:]+)\&style\=flat-square'
    match = re.search(pattern, readme)
    if match:
        now = get_time().replace(' ', '%20')
        readme = re.sub(pattern, 'label=Vercel%20' + now + '&style=flat-square', readme)
    with open(readme_path, 'w') as f:
        f.write(readme)

if __name__ == '__main__':
    main()