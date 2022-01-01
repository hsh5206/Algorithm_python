# 포도주 시식

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

dp = [[0]*2 for _ in range(N)]

if N == 1:
    print(arr[0])
else:
    dp[0][0] = arr[0]
    dp[0][1] = arr[0]
    dp[1][0] = arr[1]
    dp[1][1] = dp[0][1] + arr[1]

    result = dp[1][1]
    for i in range(2, N):
        dp[i][0] = dp[i-2][1] + arr[i]
        dp[i][1] = dp[i-1][0] + arr[i]
        result = max(result, max(dp[i]))

    print(result)

print(dp)
