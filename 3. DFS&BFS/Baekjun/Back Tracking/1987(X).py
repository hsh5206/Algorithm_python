# 알파벳

import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [] * N
for _ in range(N):
    arr.append(input().strip())
visited = [[False] * M for _ in range(N)]
history = []
result = -1

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def bfs():
    global result
    history.append(arr[0][0])
    q = deque()
    q.append((0, 0, history, visited))
    visited[0][0] = True
    while q:
        x, y, temp, vist = q.popleft()
        result = max(result, len(temp))
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if vist[nx][ny] == False:
                    if arr[nx][ny] not in temp:

                        temp_visited = [[False] * M for _ in range(N)]
                        for i in range(N):
                            for j in range(M):
                                temp_visited[i][j] = visited[i][j]
                        temp_visited[nx][ny] = True

                        temp_history = []
                        for i in range(len(temp)):
                            temp_history.append(temp[i])
                        temp_history.append(arr[nx][ny])

                        q.append((nx, ny, temp_history, temp_visited))


bfs()
print(result)
