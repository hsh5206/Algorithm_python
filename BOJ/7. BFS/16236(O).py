# 아기 상어
import sys
from collections import deque
MAX = sys.maxsize
input = sys.stdin.readline
N = int(input())
arr = deque()
fish = []
now_x = 0
now_y = 0
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(N):
        if arr[i][j] != 0 and arr[i][j] != 9:
            fish.append((i, j))
        elif arr[i][j] == 9:
            now_x = i
            now_y = j
            arr[i][j] = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
fish.sort()


def bfs():
    isEat = True
    big = 2
    eat_num = 0
    while isEat:
        if big == eat_num:
            big += 1
            eat_num = 0
        q = deque()
        q.append((now_x, now_y))
        time = [[MAX] * N for _ in range(N)]
        time[now_x][now_y] = 1
        while q:
            x, y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if time[nx][ny] == MAX and arr[nx][ny] <= big:
                        time[nx][ny] = time[x][y] + 1
                        q.append((nx, ny))
        eat_x = 0
        eat_y = 0
        minimum = MAX
        for x, y in fish:
            if arr[x][y] != 0 and arr[x][y] < big:
                if minimum > time[x][y]:
                    minimum = time[x][y]
                    eat_x = x
                    eat_y = y
        if minimum != MAX:
            eat(eat_x, eat_y, minimum)
            eat_num += 1
        else:
            isEat = False


def eat(x, y, len):
    global result
    global now_x
    global now_y
    result += (len-1)
    now_x = x
    now_y = y
    arr[x][y] = 0


result = 0
bfs()
print(result)
