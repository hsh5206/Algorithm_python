# 오큰수

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
result = [-1] * N
q = []

q.append(0)
for i in range(1, N):
    while q and arr[q[-1]] < arr[i]:
        result[q.pop()] = arr[i]
    q.append(i)

print(*result)
