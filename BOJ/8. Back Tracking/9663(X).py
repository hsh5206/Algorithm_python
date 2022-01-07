# N-Queen

import sys
sys.setrecursionlimit(10**5)


def check(r, c):
    for i in range(1, r+1):
        if board[r-i] == c-i or board[r-i] == c + i:
            return False
    return True


def dfs(row):
    global count

    if row >= n:
        count += 1
    else:
        for i in range(n):

            # 열 방향 체크
            if col_visited[i] == True:
                continue
            else:
                if check(row, i) == True:
                    col_visited[i] = True
                    board[row] = i
                    dfs(row+1)
                    col_visited[i] = False


n = int(sys.stdin.readline())
board = [-1] * n
col_visited = [False] * n
count = 0

dfs(0)
print(resu)
