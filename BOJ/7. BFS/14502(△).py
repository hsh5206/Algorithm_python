# 연구소

import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

max_result = 0
k = []


def bfs():
    global max_result
    result = 0

    temp = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            temp[i][j] = arr[i][j]

    q = deque()
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:
                q.append((i, j))

    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    q.append((nx, ny))

    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                result += 1

    max_result = max(max_result, result)


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(cnt + 1)
                arr[i][j] = 0


wall(0)
print(max_result)
