# Puyo Puyo

from collections import deque
import sys
input = sys.stdin.readline
N = 12
M = 6
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
arr = []
for _ in range(12):
    arr.append(list(input().strip()))
result = 0


def check():
    isExplode = False
    global result
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] != '.' and not visited[i][j]:
                color = arr[i][j]
                exp = [(i, j)]
                q = deque()
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    visited[x][y] = True
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                            if arr[nx][ny] == color:
                                q.append((nx, ny))
                                exp.append((nx, ny))
                                visited[nx][ny] = True
                if len(exp) >= 4:
                    explode(exp)
                    isExplode = True
    if isExplode:
        result += 1
        gravity()
        check()


def explode(exp):
    while exp:
        x, y = exp.pop()
        arr[x][y] = '.'


def gravity():
    for x in range(N-2, -1, -1):
        for y in range(M-1, -1, -1):
            if arr[x][y] != '.' and arr[x+1][y] == '.':
                q = [(x, y)]
                while q:
                    i, j = q.pop()
                    if i+1 < N and arr[i+1][j] == '.':
                        arr[i+1][j] = arr[i][j]
                        arr[i][j] = '.'
                        q.append((i+1, j))


check()
print(result)
