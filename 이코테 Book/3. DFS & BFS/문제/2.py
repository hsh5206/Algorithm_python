# 미로탈출

from collections import deque


def dfs(x, y):
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= N or ny <= -1 or ny >= M:
                continue
            if graph[nx][ny] == 0:
                continue
            elif graph[nx][ny] == 1:
                queue.append([nx, ny])
                graph[nx][ny] += graph[x][y]
    return graph[N-1][M-1]


N, M = map(int, input.split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

print(dfs(0, 0))
