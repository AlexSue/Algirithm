import json
filename = 'T2019_4.json'
with open(filename) as f:
    label = json.load(f)
# 遍历列表的每个元素，每个元素是一个GDP数据项
print(label)
print('x:')
for t in label:
    print(t['x'])
print('\n')

print('y:')
for t in label:
    print(t['y'])
print('\n')

print('w:')
for t in label:
    print(t['w'])
print('\n')

print('h:')
for t in label:
    print(t['h'])
print('\n')

print('class:')
for t in label:
    print(t['class'])
print('\n')
