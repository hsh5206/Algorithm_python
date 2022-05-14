def solution(land):
    N, M = len(land), len(land[0])
    dp = [[0 for _ in range(M)] for _ in range(N)]
    for j in range(M):
        dp[0][j] = land[0][j]
    for i in range(1, N):
        for j in range(M):
            dp[i][j] = max(dp[i-1][:j]+dp[i-1][j+1:])+land[i][j]
    return max(dp[-1])
