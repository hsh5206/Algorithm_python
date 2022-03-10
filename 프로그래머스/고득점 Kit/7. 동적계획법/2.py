# 정수 삼각형
def solution(triangle):
    N = len(triangle)
    for i in range(N):
        triangle[i] = [0] + triangle[i] + [0]
    dp = [[0] * len(x) for x in triangle]
    dp[0][1] = triangle[0][1]
    for i in range(1, N):
        for j in range(1, len(dp[i])-1):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    return max(dp[N-1])
