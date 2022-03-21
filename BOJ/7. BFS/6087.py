# 레이저 통신
from collections import deque
import sys
input = sys.stdin.readline
MAX = sys.maxsize

M, N = map(int, input().split())
arr = []
C = []
for i in range(N):
    arr.append(list(input().strip()))
    for j in range(M):
        if arr[i][j] == 'C':
            C.append((i, j))
start, end = C[0], C[1]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(a, b):
    global answer
    q = deque()
    q.append((a, b, -1, 0))
    visited = [[0] * M for _ in range(N)]
    visited[a][b] = 0
    while q:
        x, y, dir, result = q.popleft()
        if (x, y) == end:
            answer = min(answer, result)
            continue
        for ndir in range(4):
            nx = x + dx[ndir]
            ny = y + dy[ndir]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != '*':
                if result == visited[x][y]:
                    if not visited[nx][ny]:
                        if dir == -1 or dir == ndir:
                            visited[nx][ny] = result
                            q.append((nx, ny, ndir, result))
                        elif dir != ndir:
                            visited[nx][ny] = result + 1
                            q.append((nx, ny, ndir, result + 1))
                    else:
                        if dir == ndir and visited[nx][ny] >= result:
                            visited[nx][ny] = result
                            q.append((nx, ny, ndir, result))
                        elif dir != ndir and visited[nx][ny] >= result + 1:
                            visited[nx][ny] = result + 1
                            q.append((nx, ny, ndir, result + 1))


answer = MAX
bfs(start[0], start[1])
print(answer)
