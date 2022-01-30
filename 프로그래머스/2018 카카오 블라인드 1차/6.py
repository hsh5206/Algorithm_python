# 프렌즈4블록
from collections import deque

dx = [0, 1, 1]
dy = [1, 0, 1]
break_block_list = []


def solution(n, m, board):
    answer = 0
    board_t = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            board_t[i][j] = board[i][j]

    while True:
        for i in range(n):
            for j in range(m):
                if board_t[i][j] != 0:
                    isFour(i, j, board_t, n, m)
        answer += break_block(board_t, n, m)
        if not move(board_t, n, m,):
            break
    return answer


def isFour(i, j, board, n, m):
    broke = [(i, j)]
    for k in range(3):
        x = i + dx[k]
        y = j + dy[k]
        if 0 <= x < n and 0 <= y < m:
            if board[i][j] == board[x][y]:
                broke.append((x, y))
    if len(broke) == 4:
        break_block_list.append(broke)


def break_block(board, n, m):
    temp = 0
    while break_block_list:
        broke = break_block_list.pop()
        while broke:
            x, y = broke.pop()
            if board[x][y] != 0:
                board[x][y] = 0
                temp += 1
    return temp


def move(board, n, m):
    isMove = False
    for i in range(n-2, -1, -1):
        for j in range(m-1, -1, -1):
            if board[i][j] != 0 and board[i+1][j] == 0:
                isMove = True
                temp = i
                while temp+1 < n and board[temp+1][j] == 0:
                    board[temp+1][j] = board[temp][j]
                    board[temp][j] = 0
                    temp += 1
    return isMove
