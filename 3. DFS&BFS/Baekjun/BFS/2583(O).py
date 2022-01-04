# 영역 구하기

from collections import deque
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
sizes = []


def bfs(a, b):
    size = 1
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    size += 1
    sizes.append(size)


for k in range(K):
    x, y, a, b = map(int, input().split())
    i = N-y - 1
    j = x
    n = N-b
    m = a - 1
    for t in range(n, i+1):
        for k in range(j, m+1):
            arr[t][k] = 1

result = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and visited[i][j] == False:
            bfs(i, j)
            result += 1


sizes.sort()
print(result)
for size in sizes:
    print(size, end=" ")
