# 계단 오르기

import sys
input = sys.stdin.readline
N = int(input())
arr = [0] * 301
for i in range(N):
    arr[i] = int(input())

dp = [[0]*2 for _ in range(301)]
dp[0][0] = arr[0]
dp[0][1] = arr[0]
dp[1][0] = arr[1]
dp[1][1] = arr[0] + arr[1]

for i in range(2, N):
    dp[i][0] = max(dp[i-2][0] + arr[i], dp[i-2][1] + arr[i])
    dp[i][1] = dp[i-1][0] + arr[i]

result = max(dp[N-1][0], dp[N-1][1])

print(result)
