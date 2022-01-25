# 테트로미노
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = [[False] * M for _ in range(N)]


def choose_block(x, y, count, temp):
    global result
    if count == 4:
        result = max(result, temp)
        return
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            choose_block(nx, ny, count+1, temp+arr[nx][ny])


result = 0
for i in range(N):
    for j in range(M):
        result = max(result, choose_four_block(i, j))

print(result)
