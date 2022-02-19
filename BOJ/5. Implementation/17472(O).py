# 다리 만들기 2
from collections import deque
import sys
input = sys.stdin.readline
MAX = sys.maxsize
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, M = map(int, input().split())

land = []
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(M):
        if arr[i][j] == 1:
            land.append((i, j))


def find_land(visited, a, b, num):
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = True
                arr[nx][ny] = num
                start.append((nx, ny, num))
                q.append((nx, ny))


def find_parent(x):
    if x != island[x]:
        island[x] = find_parent(island[x])
    return island[x]


def union_parent(x, y):
    a, b = find_parent(x), find_parent(y)
    if a > b:
        island[a] = b
    if a < b:
        island[b] = a


def make_straight(nx, ny, dx, dy, num, temp):
    global result
    nx += dx
    ny += dy
    if 0 <= nx < N and 0 <= ny < M:
        if arr[nx][ny] == 0:
            temp[nx][ny] = temp[nx - dx][ny - dy] + 1
            make_straight(nx, ny, dx, dy, num, temp)
        elif temp[nx-dx][ny-dy] >= 2:
            bridge.append((temp[nx-dx][ny-dy], num, arr[nx][ny]))
            return


def make_bridge():
    for x, y, num in start:
        temp = [[0] * M for _ in range(N)]
        for dx, dy in direction:
            make_straight(x, y, dx, dy, num, temp)


def check_all_connected():
    temp = 0
    for i in range(1, num_island+1):
        if i == 1:
            temp = find_parent(i)
        elif temp != find_parent(i):
            return False
    return True


start = []
visited = [[False] * M for _ in range(N)]
num_island = 1
for i, j in land:
    if not visited[i][j]:
        visited[i][j] = True
        arr[i][j] = num_island
        start.append((i, j, num_island))
        find_land(visited, i, j, num_island)
        num_island += 1
num_island -= 1

direction = [[0, -1], [-1, 0], [0, 1], [1, 0]]
island = [i for i in range(num_island+1)]


bridge = []
make_bridge()
bridge.sort()

result = 0
for len, start, end in bridge:
    if find_parent(start) != find_parent(end):
        result += len
        union_parent(start, end)

if check_all_connected():
    print(result)
else:
    print(-1)
