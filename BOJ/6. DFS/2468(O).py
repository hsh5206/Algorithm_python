# 안전 영역
'''내가 푼 풀이
import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)


def dfs(x, y):
    if x < 0 or y < 0 or x >= N or y >= N:
        return False
    elif visited[x][y] == True or arr[x][y] == 0:
        return False
    else:
        visited[x][y] = True
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True


def rain():
    for i in range(N):
        for j in range(N):
            temp = arr[i][j] - 1
            if temp < 0:
                arr[i][j] = 0
            else:
                arr[i][j] = temp


N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = 0
flag = 0
while True:
    flag = 0
    temp = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if dfs(i, j):
                    temp += 1

    if result < temp:
        result = temp

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                flag = 1
                break

    if flag == 0:
        break

    rain()

print(result)
'''

import sys
sys.setrecursionlimit(100000)
r = sys.stdin.readline

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y, h):

    for m in range(4):
        nx = x + dx[m]
        ny = y + dy[m]

        if (0 <= nx < N) and (0 <= ny < N) and not visit[nx][ny] and zone[nx][ny] > h:
            visit[nx][ny] = True
            dfs(nx, ny, h)


N = int(r())
zone = [list(map(int, r().split())) for _ in range(N)]

ans = 1
for k in range(max(map(max, zone))):
    visit = [[False]*N for _ in range(N)]
    safe = 0
    for i in range(N):
        for j in range(N):
            if zone[i][j] > k and not visit[i][j]:
                safe += 1
                visit[i][j] = True
                dfs(i, j, k)
    ans = max(ans, safe)

print(ans)
