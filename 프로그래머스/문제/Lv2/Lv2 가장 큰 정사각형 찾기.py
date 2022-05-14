# https://programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):
    N, M = len(board), len(board[0])
    dp = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        dp[i][0] = board[i][0]
    for j in range(M):
        dp[0][j] = board[0][j]
    for i in range(1, N):
        for j in range(1, M):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
    result = 0
    for x in dp:
        result = max(result, max(x))
    return result**2


print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))
