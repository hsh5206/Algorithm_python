# 벽 부수고 이동하기
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
result = []
broke = 1

arr = [] * N
for _ in range(N):
    arr.append(input().strip())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs():
    global result
    q = deque()
    q.append((0, 0, broke, 1))
    while q:
        x, y, br, re = q.popleft()
        if x == N-1 and y == M-1:
            result.append(re)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == '0':
                    q.append((nx, ny, br, re+1))
                elif br == 1:
                    q.append((nx, ny, br-1, re+1))


bfs()
if result:
    print(min(result))
else:
    print("-1")
