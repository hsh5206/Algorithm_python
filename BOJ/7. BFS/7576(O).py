# 토마토
from collections import deque


def bfs():
    queue = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            elif arr[nx][ny] == -1:
                continue
            elif arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))


M, N = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs()
result = 0
for i in range(N):
    if 0 in arr[i]:
        result = 0
        break
    elif result < max(arr[i]):
        result = max(arr[i])

print(result - 1)
