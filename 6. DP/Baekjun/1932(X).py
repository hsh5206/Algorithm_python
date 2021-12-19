# 정수 삼각형

import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
result = []

dx = [1, 1]
dy = [0, 1]


def bfs(start):
    q = deque()
    q.append((start, 0, 0))
    while q:
        cost, x, y = q.popleft()
        if x == N-1:
            result.append(cost)
            continue
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= N-1 and ny <= nx:
                temp = cost + arr[nx][ny]
                q.append((temp, nx, ny))


start = int(input())
arr = [start]
for _ in range(N - 1):
    arr.append(list(map(int, input().split())))

bfs(start)
print(max(result))
