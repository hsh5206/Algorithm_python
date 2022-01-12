# 제로

import sys
input = sys.stdin.readline
K = int(input())
arr = []
for _ in range(K):
    arr.append(int(input()))
    if arr[-1] == 0:
        arr.pop()
        arr.pop()

result = 0
for temp in arr:
    result += temp

print(result)
