# 낚시왕
import sys
input = sys.stdin.readline

N, M, S = map(int, input().split())
arr = [[[] for _ in range(M+1)] for _ in range(N+1)]
shark = []
for _ in range(S):
    n, m, speed, direction, big = map(int, input().split())
    arr[n][m].append((speed, direction, big))
    shark.append([n, m, speed, direction, big])


fishing_shark = [1, 0]
shark_move = [[], [-1, 0], [1, 0], [0, 1], [0, -1]]
check = []


def fishing(now):
    global result
    for i in range(1, N+1):
        if arr[i][now]:
            speed, dir, big = arr[i][now].pop()
            result += big
            break


def move_shark():
    for k in range(len(shark)):
        if arr[n][m]:
            speed, dir, big = arr[n][m].pop()
            nn = n
            nm = m
            for _ in range(speed):
                nn += shark_move[dir][0]
                nm += shark_move[dir][1]
                if 0 < nn <= N and 0 < nm <= M:
                    continue
                else:
                    nn -= shark_move[dir][0]
                    nm -= shark_move[dir][1]
                    dir = change_dir(dir)
                    nn += shark_move[dir][0]
                    nm += shark_move[dir][1]
            if arr[nn][nm]:
                check.append((nn, nm))
            arr[nn][nm].append((speed, dir, big))
            shark[k][0] = nn
            shark[k][1] = nm


def change_dir(dir):
    if dir == 1:
        return 2
    elif dir == 2:
        return 1
    elif dir == 3:
        return 4
    else:
        return 3


def eat_shark():
    x, y = check.pop()
    if len(arr[x][y]) >= 2:
        speed, dir, big = arr[x][y].pop()
        while arr[x][y]:
            nspeed, ndir, nbig = arr[x][y].pop()
            if big > nbig:
                continue
            else:
                speed, dir, big = nspeed, ndir, nbig
        arr[x][y].append((speed, dir, big))


result = 0
for i in range(1, N+1):
    fishing(i)
    move_shark()
    if check:
        eat_shark()
print(result)
