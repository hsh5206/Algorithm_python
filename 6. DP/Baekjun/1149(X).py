# RGB거리

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
dp = [0] * N

dp[0] = min(arr[0])
