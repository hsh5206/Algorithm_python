# 낚시왕
import copy
import sys
from collections import deque
input = sys.stdin.readline

N, M, S = map(int, input().split())
arr = [[deque([]) for _ in range(M+1)] for _ in range(N+1)]
for _ in range(S):
    n, m, speed, direction, big = map(int, input().split())
    arr[n][m].append((speed, direction, big))

shark_move = [[], [-1, 0], [1, 0], [0, 1], [0, -1]]
check = []


def fishing(now):
    global result
    for i in range(1, N+1):
        if arr[i][now]:
            speed, dir, big = arr[i][now].pop()
            result += big
            break


def move_shark(temp):
    for n in range(1, N+1):
        for m in range(1, M+1):
            if temp[n][m]:
                temp[n][m].pop()
                speed, dir, big = arr[n][m].popleft()
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
for i in range(1, M+1):
    fishing(i)
    temp = copy.deepcopy(arr)
    move_shark(temp)
    if check:
        eat_shark()
print(result)
