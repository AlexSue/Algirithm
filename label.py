import json
filename = 'T2019_4.json'
with open(filename) as f:
    label = json.load(f)
# 遍历列表的每个元素，每个元素是一个GDP数据项
print(label)