# 단어 수학
from collections import deque
N = int(input())
arr = []
for _ in range(N):
    arr.append(deque(list(input().strip())))
alpha = {}

for i in range(N):
    j = 0
    while True:
        if len(arr[i]) == 0:
            break
        if arr[i][j] in alpha:
            alpha[arr[i].popleft()] += 10**(len(arr[i]))
        else:
            alpha[arr[i].popleft()] = 10**(len(arr[i])-1)

list = []
for i in alpha.values():
    list.append(i)
list.sort(reverse=True)

result = 0
num = 9
for i in list:
    result += i*num
    num -= 1

print(result)
