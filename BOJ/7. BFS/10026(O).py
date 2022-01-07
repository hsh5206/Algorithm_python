# 적록 색약

import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
arr = [] * N
for _ in range(N):
    arr.append(input().strip())
visited1 = [[False] * N for _ in range(N)]
visited2 = [[False] * N for _ in range(N)]
result1 = 0
result2 = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs1(a, b):
    global result1
    q = deque()
    q.append((a, b))
    visited1[a][b] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if visited1[nx][ny] == False:
                    if arr[nx][ny] == arr[x][y]:
                        visited1[nx][ny] = True
                        q.append((nx, ny))
    result1 += 1


def bfs2(a, b):
    global result2
    q = deque()
    q.append((a, b))
    visited2[a][b] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if visited2[nx][ny] == False:
                    if arr[nx][ny] == arr[x][y]:
                        visited2[nx][ny] = True
                        q.append((nx, ny))
                    elif arr[x][y] == 'R' and arr[nx][ny] == 'G':
                        visited2[nx][ny] = True
                        q.append((nx, ny))
                    elif arr[x][y] == 'G' and arr[nx][ny] == 'R':
                        visited2[nx][ny] = True
                        q.append((nx, ny))
    result2 += 1


for i in range(N):
    for j in range(N):
        if visited1[i][j] == False:
            bfs1(i, j)
        if visited2[i][j] == False:
            bfs2(i, j)


print(result1, result2)
