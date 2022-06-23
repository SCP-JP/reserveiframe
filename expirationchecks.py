import frontmatter
from datetime import datetime as dt
from pytz import timezone
import os
from pathlib import Path

reserves = Path("src/reserve").glob('**/*.md')
today = dt.now().astimezone(timezone('Asia/Tokyo')).date()
for filename in reserves:
        with open(filename, 'r', encoding='utf-8') as f:
            data = frontmatter.load(f)
        # data['endtime']が今日の日付よりも過去の日付ならファイルを削除する
        try:
            endtime = dt.strptime(data['endtime'], '%Y-%m-%d').date()
            print(filename,"\t\t" ,endtime)
            if endtime < today:
                print('{} is expired'.format(filename))
                os.remove(filename)
        except:
            print('{} is not expired'.format(filename))
