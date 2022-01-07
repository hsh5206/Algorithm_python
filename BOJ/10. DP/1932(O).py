# 정수 삼각형

import sys
input = sys.stdin.readline
N = int(input())
start = int(input())

arr = [[] for _ in range(N)]
arr[0] = list([0, start, 0])
for i in range(1, N):
    arr[i] = [0] + list(map(int, input().split())) + [0]

dp = [[0] * len(x) for x in arr]

dp[0][1] = arr[0][1]
for i in range(1, N):
    for j in range(1, len(dp[i])-1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j]

print(max(dp[N-1]))
