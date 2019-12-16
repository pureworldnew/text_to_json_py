import json
import datetime
import re

data = ''
s = ''
with open('sample.json') as json_file:
    data = json.load(json_file)

s = str(data)
s = re.sub(r"\s+", "", s)

month_array = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
now = datetime.datetime.now()
month_name = month_array[now.month-1]
filename = "adidas-us_" + str(now.year) + month_name + str(now.day) + '_' + str(now.hour) + '.' + str(now.minute) + '.' + str(now.second)

with open(filename + ".txt", "w") as fout:
    print(s, file=fout)