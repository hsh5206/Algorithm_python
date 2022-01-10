# 알고스팟

import sys
import copy
from collections import deque
INF = sys.maxsize
input = sys.stdin.readline
M, N = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().strip())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visit = [[False] * M for _ in range(N)]
result = [[INF] * M for _ in range(N)]


def bfs():
    q = deque()
    q.append((0, 0))
    result[0][0] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if result[nx][ny] == INF:
                    if arr[nx][ny] == 0:
                        result[nx][ny] = result[x][y]
                        q.appendleft((nx, ny))
                    elif arr[nx][ny] == 1:
                        result[nx][ny] = result[x][y] + 1
                        q.append((nx, ny))


bfs()
print(result[N-1][M-1])
