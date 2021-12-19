# 계단 오르기

import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

dp = [0] * N
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[1]+arr[2], arr[0]+arr[2])

for i in range(3, N):
    dp[i] = max((dp[i-2]+arr[i]), (dp[i-3]+arr[i-1]+arr[i]))
    if i == N-1:
        dp[i] = max((dp[i-2]+arr[i]), (dp[i-3]+arr[i-1]+arr[i]))

print(dp[N-1])
