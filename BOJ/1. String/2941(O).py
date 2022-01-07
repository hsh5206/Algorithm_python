# 크로아티아 알파벳
'''
from collections import deque
alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

arr = input()
result = 0
q = deque()
for x in arr:
    q.append(x)
    if len(q) == 3:
        a = q.popleft()
        b = q.popleft()
        temp = -1
        if a+b+q[0] == 'dz=':
            result += 1
            temp = 0
            q.popleft()
        else:
            for y in alpha:
                if a+b == y:
                    temp = 1
                    break
        if temp == -1:
            result += 1
            q.appendleft(b)
        elif temp == 1:
            result += 1

if len(q) == 2:
    a = q.popleft()
    b = q.popleft()
    temp = -1
    for y in alpha:
        if a+b == y:
            temp = 1
            break
    if temp == 1:
        result += 1
    else:
        result += 2
else:
    result += 1

print(result)
'''
# replace 함수 사용
alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
arr = input()
for x in alpha:
    arr = arr.replace(x, '*')

print(len(arr))
