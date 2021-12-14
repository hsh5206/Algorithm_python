# 뱀

from collections import deque

N = int(input())
arr = [[0] * N for _ in range(N)]
arr[0][0] = 1

K = int(input())
isApple = [[False] * N for _ in range(N)]
for i in range(K):
    x, y = map(int, input().split())
    isApple[x - 1][y - 1] = True

O = int(input())
order = []
for _ in range(O):
    a, b = input().split()
    a = int(a)
    order.append([a, b])

count = 0
x = 0
y = 0
direction = ''
q = deque()
dx = 0
dy = 1
while True:
    q.append([x, y])
    nx = x + dx
    ny = y + dy

    if nx < 0 or ny < 0 or nx >= N or ny >= N or arr[nx][ny] == 1:
        break

    arr[nx][ny] = 1

    if not isApple[nx][ny]:
        tail_x, tail_y = q.popleft()
        arr[tail_x][tail_y] = 0
    else:
        isApple[nx][ny] = False

    for o in order:
        o[0] -= 1
        if (o[0] == 0):
            direction = o[1]

    if direction:
        if direction == 'L':
            if dx == 0 and dy == 1:
                dx, dy = -1, 0
            elif dx == 1 and dy == 0:
                dx, dy = 0, 1
            elif dx == 0 and dy == -1:
                dx, dy = 1, 0
            else:
                dx, dy = 0, -1
        else:
            if dx == 0 and dy == 1:
                dx, dy = 1, 0
            elif dx == 1 and dy == 0:
                dx, dy = 0, -1
            elif dx == 0 and dy == -1:
                dx, dy = -1, 0
            else:
                dx, dy = 0, 1
        direction = ''

    x, y = nx, ny
    count += 1

print(count + 1)
