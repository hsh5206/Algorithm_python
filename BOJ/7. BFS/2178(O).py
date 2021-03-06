# 미로 탐색
import sys
from collections import deque
input = sys.stdin.readline


def go(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= N or ny <= -1 or ny >= M:
                continue
            if arr[nx][ny] == 0:
                continue
            elif arr[nx][ny] == 1:
                q.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1


N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().strip())))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

go(0, 0)
print(arr[N-1][M-1])
