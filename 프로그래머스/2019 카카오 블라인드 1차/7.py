# 블록게임
import copy
dx = [[0, 0, 0, 1, 1, 1], [0, 0, 1, 1, 2, 2]]
dy = [[0, 1, 2, 0, 1, 2], [0, 1, 0, 1, 0, 1]]
answer = 0


def solution(board):
    N = len(board)
    global answer

    while True:
        if not drop_block(board):
            break
    return answer


def drop_block(arr):
    N = len(arr)
    for j in range(N):
        for i in range(N):
            if arr[i][j] == -1:
                continue
            if arr[i][j] != 0:
                break
            arr[i][j] = -1
    return check(arr)


def check(arr):
    N = len(arr)
    for i in range(N):
        for j in range(N):
            isBreak = True
            if arr[i][j] != 0:
                t = -1
                temp = 0
                for k in range(len(dx[0])):
                    nx = i + dx[0][k]
                    ny = j + dy[0][k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] == 0:
                            isBreak = False
                            break
                        elif arr[nx][ny] != -1:
                            if t == -1:
                                t = arr[nx][ny]
                            elif arr[nx][ny] != t:
                                isBreak = False
                                break
                            temp += 1
                    else:
                        isBreak = False
                    if not isBreak:
                        break
                if temp != 4:
                    isBreak = False
                if isBreak:
                    break_block(arr, i, j, 0)
                    return True

            isBreak = True
            if arr[i][j] != 0:
                t = -1
                temp = 0
                for k in range(len(dx[1])):
                    nx = i + dx[1][k]
                    ny = j + dy[1][k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] == 0:
                            isBreak = False
                            break
                        elif arr[nx][ny] != -1:
                            if t == -1:
                                t = arr[nx][ny]
                            elif arr[nx][ny] != t:
                                isBreak = False
                                break
                            temp += 1
                    else:
                        isBreak = False
                    if not isBreak:
                        break
                if temp != 4:
                    isBreak = False
                if isBreak:
                    break_block(arr, i, j, 1)
                    return True
    return False


def break_block(arr, x, y, k):
    global answer
    for t in range(len(dx[k])):
        nx = x + dx[k][t]
        ny = y + dy[k][t]
        arr[nx][ny] = 0
    answer += 1


print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [
      0, 0, 0, 0, 0, 4, 4, 0, 0, 0], [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5], [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]))
