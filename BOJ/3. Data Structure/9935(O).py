# 문자열 폭발
'''
str = input().strip()
bomb = input().strip()

while True:
    if bomb not in str:
        break
    str = str.replace(bomb, '')

if str:
    print(str)
else:
    print('FRULA')
'''

str = input().strip()
bomb = list(input().strip())

result = []
for i in range(len(str)):
    result.append(str[i])
    if result[-len(bomb):] == bomb:
        for _ in range(len(bomb)):
            result.pop()
if result:
    print(*result, sep='')
else:
    print('FRULA')
