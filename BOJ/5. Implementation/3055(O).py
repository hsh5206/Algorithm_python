# 탈출

import sys
import copy
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(input().strip()))
water_vist = [[False] * M for _ in range(N)]
s_vist = [[False] * M for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def water(x, y, water_vist):
    if water_vist[x][y]:
        return
    water_vist[x][y] = True
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if not water_vist[nx][ny]:
                if arr[nx][ny] == '.' or arr[nx][ny] == 'S':
                    arr[nx][ny] = '*'
                    water_vist[nx][ny] = True


def move(x, y, s_vist):
    global isTrue
    if s_vist[x][y]:
        return
    s_vist[x][y] = True
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if not s_vist[nx][ny]:
                if arr[nx][ny] == '.':
                    s_vist[nx][ny] = True
                    arr[nx][ny] = 'S'
                if arr[nx][ny] == 'D':
                    isTrue = False
                    return


isTrue = True
isFalse = False
result = 0
while True:
    isFalse = True
    temp = copy.deepcopy(s_vist)
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'S':
                isFalse = False
                move(i, j, temp)
    temp = copy.deepcopy(water_vist)
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '*':
                water(i, j, temp)

    result += 1
    if not isTrue:
        break
    if isFalse:
        break

if isFalse:
    print('KAKTUS')
else:
    print(result)
