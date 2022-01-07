# 피보나치 함수

T = int(input())
arr = []
for _ in range(T):
    arr.append(int(input()))

dp = [[0] * 2 for _ in range(41)]
dp[0][0] = 1
dp[0][1] = 0
dp[1][0] = 0
dp[1][1] = 1

for t in range(T):
    x = arr[t]
    for i in range(2, x + 1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]
    print(dp[x][0], dp[x][1])
