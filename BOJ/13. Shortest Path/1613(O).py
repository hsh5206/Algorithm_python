# 역사
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

arr = [[False]*(N+1) for _ in range(N+1)]
for a in range(1, N+1):
    for b in range(1, N + 1):
        if a == b:
            arr[a][b] = False

for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = True

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][k] and arr[k][j]:
                arr[i][j] = True

K = int(input())
for _ in range(K):
    i, j = map(int, input().split())
    if arr[i][j] and not arr[j][i]:
        print(-1)
    elif not arr[i][j] and arr[j][i]:
        print(1)
    elif not arr[i][j] and not arr[j][i]:
        print(0)
