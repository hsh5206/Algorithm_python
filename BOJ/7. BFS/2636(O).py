# 치즈
import sys
import copy
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def updateAir():
    q = deque()
    q.append((0, 0))
    temp[0][0] = 2
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    q.append((nx, ny))


def melt(x, y):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if temp[nx][ny] == 2:
                arr[x][y] = 0


def allMelt():
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                return False
    return True


result = 0
before = 0
while True:
    temp = copy.deepcopy(arr)
    updateAir()
    if allMelt():
        break
    before = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                before += 1
    for i in range(1, N):
        for j in range(1, M):
            if arr[i][j] == 1:
                melt(i, j)
    result += 1


print(result)
print(before)
