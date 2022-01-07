# 아기 상어

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = [] * N
for _ in range(N):
    arr.append(list(map(int, input().split())))
size = 2
eat = 0
result = [[0] * N for _ in range(N)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def bfs(a, b):
    global size, eat
    q = deque()
    q.append((a, b))
    result[a][b] = 1
    arr[a][b] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if result[nx][ny] == 0:
                    if arr[nx][ny] == 0 or arr[nx][ny] == size:
                        result[nx][ny] = result[x][y] + 1
                        q.append((nx, ny))
                    elif arr[nx][ny] < size:
                        result[nx][ny] = result[x][y] + 1
                        q.append((nx, ny))
                        eat += 1
                        if size == eat:
                            size += 1
                            eat = 0
                        arr[nx][ny] = 9
                        return result[nx][ny]


rs = 0
isTrue = True
while isTrue:
    isFin = False
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                rs += (bfs(i, j) - 1)
                result = [[0] * N for _ in range(N)]
                isFin = True
                break
        if isFin:
            break
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0 or arr[i][j] == 9:
                isTrue = False
            elif arr[i][j] < size:
                isTrue = True
                break
        if isTrue:
            break

if rs == -1:
    print(0)
else:
    print(rs)
