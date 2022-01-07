# 쉬운 최단거리
import sys
from collections import deque


def bfs(x, y):
    visited = [[-1]*M for _ in range(N)]
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < N) and (0 <= ny < M):
                if arr[nx][ny] == 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])
                elif arr[nx][ny] == 0:
                    visited[nx][ny] = 0
    return visited


N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = [[-1]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            result = bfs(i, j)

for i in range(N):
    for j in range(M):
        # 갈 수 없는 땅중 원래 벽인 부분을 고려
        if result[i][j] == -1 and arr[i][j] == 0:
            result[i][j] = 0
        print(result[i][j], end=' ')
    print()
