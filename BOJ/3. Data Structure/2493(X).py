# 탑

import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
q = []
result = [0 for _ in range(N)]

for i in range(N):
    while q:
        if q[-1][1] > arr[i]:
            result[i] = q[-1][0] + 1
            break
        else:
            q.pop()
    q.append([i, arr[i]])

for i in range(1, len(result)):
    print(result[i], end=" ")
