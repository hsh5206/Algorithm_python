# 빙산
from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
ice = []
melt = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(M):
        if arr[i][j] != 0:
            ice.append((i, j))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def melt_check():
    for x, y in ice:
        if arr[x][y] != 0:
            zero = 0
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < M:
                    if arr[nx][ny] == 0:
                        zero += 1
            if zero != 0:
                melt.append((x, y, zero))


def melt_ice():
    while melt:
        x, y, how = melt.pop()
        arr[x][y] -= how
        if arr[x][y] < 0:
            arr[x][y] = 0


def check():
    global year
    num = 0
    visited = [[False]*M for _ in range(N)]
    melted = 0
    for x, y in ice:
        if arr[x][y] != 0 and not visited[x][y]:
            bfs(x, y, visited)
            num += 1
            # 두 덩어리 이상이면 return True
            if num > 1:
                return True
        # 녹은 개수 빙하 수 체크
        if arr[x][y] == 0:
            melted += 1
    # 다 녹았으면 0 출력, return True
    if melted == len(ice):
        year = 0
        return True
    # 그 외엔 return False
    return False


def bfs(a, b, visited):
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny] != 0:
                visited[nx][ny] = True
                q.append((nx, ny))


year = 0
while True:
    if check():
        break
    melt_check()
    melt_ice()
    year += 1

print(year)
