# 다리 만들기
from collections import deque
import sys
input = sys.stdin.readline
MAX = sys.maxsize

N = int(input())
arr = []
sea = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(N):
        if arr[i][j] == 0:
            sea.append((i, j))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
result = MAX


def bfs(a, b):
    global result
    q = deque()
    q.append((a, b))
    visited = [[0] * N for _ in range(N)]
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if arr[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                elif arr[nx][ny] == 1:
                    if check_land(a, b, nx, ny):
                        result = min(result, visited[x][y])
                        return


def check_land(a1, b1, a2, b2):
    q = deque()
    q.append((a1, b1))
    visited = [[False] * N for _ in range(N)]
    visited[a1][b1] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if arr[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    if visited[a2][b2]:
        return False
    else:
        return True


for a, b in sea:
    can = False
    for k in range(4):
        na = a + dx[k]
        nb = b + dy[k]
        if 0 <= na < N and 0 <= nb < N:
            if arr[na][nb] == 1:
                a = na
                b = nb
                can = True
    if can:
        bfs(a, b)
print(result)
