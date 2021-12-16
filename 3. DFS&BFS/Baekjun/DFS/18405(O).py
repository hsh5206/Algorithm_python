# 경쟁적 전염
import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

S, X, Y = map(int, input().split())


def virus(time):
    before = 1
    while q:
        x, y, k = q.popleft()
        if before != k and k == 1:
            time -= 1
        if time == 0:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = k
                    q.append((nx, ny, k))
        before = k


q = deque()
for k in range(1, K + 1):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == k:
                q.append((i, j, k))
virus(S)

print(arr[X-1][Y-1])
