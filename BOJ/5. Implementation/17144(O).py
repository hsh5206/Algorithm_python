# 미세먼지 안녕!

import sys
import copy
input = sys.stdin.readline
N, M, T = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def spread(x, y, temp):
    count = 0
    change = temp[x][y] // 5
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] != -1:
                count += 1
                arr[nx][ny] += change
    arr[x][y] = arr[x][y] - (change * count)


def move(flag, x, y, temp):
    if flag == 0:
        for j in range(1, M-1):
            arr[x][j+1] = temp[x][j]
        for i in range(x, 0, -1):
            arr[i-1][-1] = temp[i][-1]
        for j in range(M-1, 0, -1):
            arr[0][j-1] = temp[0][j]
        for i in range(x):
            arr[i+1][y] = temp[i][y]
        arr[x][y] = -1
        arr[x][y+1] = 0
    if flag == 1:
        for j in range(1, M-1):
            arr[x][j+1] = temp[x][j]
        for i in range(x, N-1):
            arr[i+1][-1] = temp[i][-1]
        for j in range(M-1, 0, -1):
            arr[N-1][j-1] = temp[N-1][j]
        for i in range(N-1, x, -1):
            arr[i-1][y] = temp[i][y]

        arr[x][y] = -1
        arr[x][y+1] = 0


for _ in range(T):
    temp = copy.deepcopy(arr)
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and arr[i][j] != -1:
                spread(i, j, temp)

    temp = copy.deepcopy(arr)
    flag = 0
    for i in range(N):
        if arr[i][0] == -1:
            move(flag, i, 0, temp)
            flag += 1

result = 0
for i in range(N):
    for j in range(M):
        result += arr[i][j]

print(result + 2)
