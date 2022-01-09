# 인구 이동
import sys
from collections import deque
input = sys.stdin.readline
N, L, R = map(int, input().split())
arr = [] * N
for _ in range(N):
    arr.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
result = []


def bfs(a, b):
    q = deque()
    q.append((a, b))
    result = []
    result.append((a, b))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
                if L <= abs(arr[x][y]-arr[nx][ny]) <= R:
                    visited[nx][ny] = True
                    result.append((nx, ny))
                    q.append((nx, ny))
    return result


change = 0
while True:
    visited = [[False] * N for _ in range(N)]
    isTrue = False

    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                visited[i][j] = True
                temp = bfs(i, j)
                if len(temp) > 1:
                    isTrue = True
                    num = sum([arr[x][y] for x, y in temp]) // len(temp)
                    for x, y in temp:
                        arr[x][y] = num
    if not isTrue:
        break
    change += 1

print(change)
