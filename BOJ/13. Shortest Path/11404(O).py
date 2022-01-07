# 플로이드

import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
K = int(input())
arr = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    arr[i][i] = 0

for _ in range(K):
    i, j, cost = map(int, input().split())
    arr[i][j] = min(arr[i][j], cost)

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

for i in range(1, N+1):
    for j in range(1, N+1):
        if arr[i][j] == INF:
            print(0, end=" ")
        else:
            print(arr[i][j], end=" ")
    print()
