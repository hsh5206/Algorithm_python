# 벽 부수고 이동하기
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().strip())))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs():
    global result
    q = deque()
    q.append((0, 0, 0))
    time = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    time[0][0][0] = 1
    while q:
        x, y, wall = q.popleft()
        if x == N-1 and y == M-1:
            return time[x][y][wall]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 1 and wall == 0:
                    time[nx][ny][wall+1] = time[x][y][wall] + 1
                    q.append((nx, ny, wall+1))
                elif arr[nx][ny] == 0 and time[nx][ny][wall] == 0:
                    time[nx][ny][wall] = time[x][y][wall] + 1
                    q.append((nx, ny, wall))


result = bfs()
if result:
    print(result)
else:
    print(-1)
