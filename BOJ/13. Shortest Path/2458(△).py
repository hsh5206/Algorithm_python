# 키 순서
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 0:
                if arr[i][k] == 1 and arr[k][j] == 1:
                    arr[i][j] = 1

result = 0
for i in range(1, N+1):
    sum = 0
    for j in range(1, N+1):
        sum += arr[i][j] + arr[j][i]
    if sum == N-1:
        result += 1
print(result)
