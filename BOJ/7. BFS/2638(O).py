# 치즈

import sys
from collections import deque
import copy
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def air_check(arr):
    q = deque()
    q.append((0, 0))
    arr[0][0] = 2
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 2
                    q.append((nx, ny))
    melt_check(arr)


def melt_check(arr):
    for x, y in cheese:
        if arr[x][y] == 1:
            air = 0
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < M:
                    if arr[nx][ny] == 2:
                        air += 1
            if air >= 2:
                melt.append((x, y))
    melt_cheese()


def melt_cheese():
    while melt:
        x, y = melt.pop()
        arr[x][y] = 0


N, M = map(int, input().split())
arr = []
cheese = []
melt = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(M):
        if arr[i][j] == 1:
            cheese.append((i, j))

result = 0
while True:
    is_melt_all = True
    for x, y in cheese:
        if arr[x][y] == 1:
            is_melt_all = False
            break
    if is_melt_all:
        break
    temp = copy.deepcopy(arr)
    air_check(temp)
    result += 1

print(result)
