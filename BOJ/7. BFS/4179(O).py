# 불!
from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
arr = []
now = deque()
fire = deque()
for i in range(N):
    arr.append(list(input().strip()))
    for j in range(M):
        if arr[i][j] == 'J':
            now.append((i, j))
            arr[i][j] = 1
        if arr[i][j] == 'F':
            fire.append((i, j))


def move():
    leng = len(now)
    for _ in range(leng):
        x, y = now.pop()
        if arr[x][y] != 'F':
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < M:
                    if arr[nx][ny] != '#' and arr[nx][ny] != 'F' and not visited[nx][ny]:
                        arr[nx][ny] = arr[x][y] + 1
                        visited[nx][ny] = True
                        now.appendleft((nx, ny))
                else:
                    return arr[x][y]


def fire_move():
    leng = len(fire)
    for _ in range(leng):
        x, y = fire.pop()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] != '#' and arr[nx][ny] != 'F':
                    arr[nx][ny] = 'F'
                    fire.appendleft((nx, ny))


answer = 0
visited = [[False] * M for _ in range(N)]
visited[now[0][0]][now[0][1]] = True
while True:
    answer = move()
    if answer or not now:
        break
    fire_move()

if not answer:
    print('IMPOSSIBLE')
else:
    print(answer)
