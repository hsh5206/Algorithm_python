# 보물섬

from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited = [[0]*M for _ in range(N)]
    visited[x][y] = 1
    cnt = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if arr[nx][ny] == 1:
                continue
            elif arr[nx][ny] == 'L' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                cnt = max(cnt, visited[nx][ny])
                queue.append((nx, ny))
    return cnt - 1


N, M = map(int, input().split())
arr = [[0]*M for _ in range(N)]
for i in range(N):
    arr[i] = list(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            result = max(result, bfs(i, j))

print(result)
