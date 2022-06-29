# data/*.csv -> src/reserve/_default/*md
# ---
# url: _default:{2}
# user: {1}.replace('_', '-').replace(' ', '-').lower()
# starttime: "{0}"
# endtime: "{4}"
# ---
# <reserve />
# に置き換える．

import csv
import os
import re
from datetime import datetime

def main():
    """
    main function
    """
    # read csv
    csv_file = open('data/翻訳予約リスト.csv', 'r', encoding='utf-8')
    reader = csv.reader(csv_file)
    next(reader)
    data = [row for row in reader]
    csv_file.close()
    print(data)
    # read template
    template_file = open('src/reserve/_default/reserve.md', 'r', encoding='utf-8')
    template = template_file.read()
    template_file.close()
    for row in data:
        # replace
        url = row[2]
        user = row[1].replace('_', '-').replace(' ', '-').lower()
        # 日付形式を%d/%m/%Yから%Y-%m-%d変更する
        starttime = datetime.strptime(row[0], '%Y/%m/%d').strftime('%Y-%m-%d')
        endtime = datetime.strptime(row[4], '%Y/%m/%d').strftime('%Y-%m-%d')
        # write
        output_file = open('src/reserve/_default/{}.md'.format(url), 'w', encoding='utf-8')
        output_file.write(template.replace('{url}', url).replace('{user}', user).replace('{starttime}', '"'+starttime+'"').replace('{endtime}', '"'+endtime+'"'))
        output_file.close()




if __name__ == '__main__':
    main()