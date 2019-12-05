import json
import datetime
with open("adc_abck.txt", "r") as fin:
    output = {}
    json_content = []

    for line in fin:
        json_item = {}
        line = line.replace('\n', '')
        json_item["cookie"] = line
        json_item["timestamp"] = 1575308939983
        json_content.append(json_item)

    output["adidas-us"] = json_content
    output = json.dumps(output, separators=(',', ':'))

month_array = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
now = datetime.datetime.now()
month_name = month_array[now.month-1]
filename = "adidas-us_" + str(now.year) + month_name + str(now.day) + '_' + str(now.hour) + '.' + str(now.minute) + '.' + str(now.second)

with open(filename + ".json", "w") as fout:
    print(output, file=fout)