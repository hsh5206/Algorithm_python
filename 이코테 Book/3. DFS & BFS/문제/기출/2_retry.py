# 연구소
# DFS

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
temp = [[0]*M for _ in range(N)]
count = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
result = 0


def virus(x, y):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)


def getArea():
    num = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                num += 1
    return num


def dfs(count):
    global result
    if count == 3:
        for i in range(N):
            for j in range(M):
                temp[i][j] = arr[i][j]
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 2:
                    virus(i, j)
        result = max(result, getArea())
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                count += 1
                arr[i][j] = 1
                dfs(count)
                count -= 1
                arr[i][j] = 0


dfs(0)
print(result)
