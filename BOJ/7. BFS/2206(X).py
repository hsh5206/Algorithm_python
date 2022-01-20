# 벽 부수고 이동하기

import sys
from collections import deque
import copy
input = sys.stdin.readline
MAX = sys.maxsize


def bfs(arr):
    global result
    q = deque()
    q.append((0, 0))
    arr[0][0] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] + 1
                    q.append((nx, ny))
    if arr[N-1][M-1] != 0:
        result = min(result, arr[N-1][M-1])


def break_wall():
    temp = copy.deepcopy(arr)
    bfs(temp)
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                arr[i][j] = 0
                temp = copy.deepcopy(arr)
                bfs(temp)
                arr[i][j] = 1


N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().strip())))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
result = MAX

break_wall()
if result == MAX:
    print(-1)
else:
    print(result)
