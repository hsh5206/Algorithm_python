# 가장 긴 증가하는 부분 수열
import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
