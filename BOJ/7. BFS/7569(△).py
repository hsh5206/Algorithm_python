# 토마토

import sys
from collections import deque
input = sys.stdin.readline

N, M, H = map(int, input().split())
arr = [[] for _ in range(H)]
for z in range(H):
    for x in range(M):
        arr[z].append(list(map(int, input().split())))

dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
q = deque()


def bfs():
    while q:
        x, y, z = q.popleft()
        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                if arr[nz][nx][ny] == 0:
                    arr[nz][nx][ny] = arr[z][x][y] + 1
                    q.append((nx, ny, nz))
                    visited[z][x][y] = True


visited = [[[False]*N for _ in range(M)] for _ in range(H)]
for k in range(H):
    for i in range(M):
        for j in range(N):
            if arr[k][i][j] == 1:
                q.append((i, j, k))

isTrue = False
bfs()
result = 0
for k in range(H):
    for i in range(M):
        for j in range(N):
            if arr[k][i][j] == 0:
                isTrue = True
                break
            result = max(result, arr[k][i][j])

if isTrue == True:
    print(-1)
else:
    print(result - 1)
