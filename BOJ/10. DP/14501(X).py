# 퇴사

N = int(input())
arr = [[0]*2 for _ in range(N+1)]
for i in range(1, N+1):
    t, p = map(int, input().split())
    arr[i][0] = t
    arr[i][1] = p

dp = [0] * (N+1)
if arr[i][0] == 1:
    dp[i] = arr[i][1]

for i in range(1, len(arr)):
    if arr[i-1][0] == i:
        if arr[i][0] == 1:
            dp[i] = dp[i-1] + max(arr[i][1], arr[i-1][1])
        else:
            dp[i] = dp[i-1] + arr[i-1][1]
    elif arr[i-1][0] < i:
        if arr[i][0] == 1:
            dp[i] = dp[i-1] + arr[i][1]
        else:
            dp[i] = dp[i-1]
    elif arr[i-1][0] > i:
        if arr[i][0] == 1:
            dp[i] = arr[i][1]
        else:
            dp[i] = dp[i-1]

print(dp)
