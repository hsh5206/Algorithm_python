# 빙산

import sys
import copy
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [] * N
for _ in range(N):
    arr.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
result = 0


def numOfZero(x, y):
    result = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if temp[nx][ny] == 0:
                result += 1
    return result


def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited = [[False] * M for _ in range(N)]
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and temp[nx][ny] != 0:
                    q.append((nx, ny))
                    temp[nx][ny] = 0
                    visited[nx][ny] = True


def checkZero():
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                return False
    return True


while True:
    if checkZero():
        result = 0
        break

    temp = copy.deepcopy(arr)
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                arr[i][j] = arr[i][j] - numOfZero(i, j)
                if arr[i][j] < 0:
                    arr[i][j] = 0

    temp = copy.deepcopy(arr)
    count = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] != 0:
                temp[i][j] = 0
                count += 1
                bfs(i, j)

    result += 1
    if count > 1:
        break


print(result)
