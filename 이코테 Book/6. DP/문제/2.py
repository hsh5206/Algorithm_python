# 개미 전사
import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))

dp = [0] * 101
dp[1] = arr[1]
for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2] + arr[i])

print(dp[N - 1])
