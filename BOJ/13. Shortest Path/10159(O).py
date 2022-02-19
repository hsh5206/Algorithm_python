# 저울
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())

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

for i in range(1, N+1):
    count = -1
    for j in range(1, N+1):
        if not arr[i][j] and not arr[j][i]:
            count += 1
    print(count)
