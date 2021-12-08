# 섬의 개수
import sys
sys.setrecursionlimit(100000)


def search(x, y):
    arr[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N) and (0 <= ny < M) and arr[nx][ny] == 1:
            search(nx, ny)


dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]

while True:
    result = 0
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break

    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                result += 1
                search(i, j)

    print(result)
