# 연구소 3
import sys
import copy
from collections import deque
input = sys.stdin.readline
MAX = sys.maxsize
N, virus_num = map(int, input().split())
arr = []
virus = []
zerocount = 0
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(N):
        if arr[i][j] == 2:
            virus.append((i, j))
        if arr[i][j] == 0:
            zerocount += 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
result = MAX


def bfs(arr):
    global result
    time = [[0] * N for _ in range(N)]
    q = deque()
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'a':
                q.append((i, j))
                time[i][j] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if time[nx][ny] == 0:
                    if arr[nx][ny] == 0 or arr[nx][ny] == 2:
                        time[nx][ny] = time[x][y] + 1
                        q.append((nx, ny))
                    else:
                        time[nx][ny] = -1
    find_min_time(arr, time)


def find_min_time(arr, time):
    global result
    temp = -1
    for i in range(N):
        for j in range(N):
            if time[i][j] == 0:
                if arr[i][j] == 0:
                    return
            elif time[i][j] != -1 and arr[i][j] != 2 and arr[i][j] != 'a':
                temp = max(temp, time[i][j])
    if result > temp - 1:
        result = min(result, temp-1)


def active_virus(arr, count, temp):
    if count == virus_num:
        bfs(arr)
        return
    for start in range(temp+1, len(virus), 1):
        x, y = virus[start]
        arr[x][y] = 'a'
        active_virus(arr, count+1, start)
        arr[x][y] = 2


temp = copy.deepcopy(arr)
active_virus(temp, 0, -1)

if zerocount == 0:
    print(0)
else:
    if result == MAX:
        print(-1)
    else:
        print(result)
