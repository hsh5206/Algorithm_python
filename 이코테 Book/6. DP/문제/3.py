# 바닥 공사
# dp[i] = dp[i-1] + dp[i-2] * 2

N = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 3
for i in range(3, N + 1):
    dp[i] = dp[i-1] + dp[i-2] * 2 % 796796  # 값이 커지니까 나머지만 취함

print(dp[N])
