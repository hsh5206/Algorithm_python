# 낚시왕
import copy
import sys
from collections import deque
input = sys.stdin.readline

N, M, S = map(int, input().split())
arr = [[deque([]) for _ in range(M+1)] for _ in range(N+1)]
shark = deque()
for _ in range(S):
    n, m, speed, direction, big = map(int, input().split())
    shark.append(n, m, speed, direction, big)

shark_move = [[], [-1, 0], [1, 0], [0, 1], [0, -1]]
check = []


def fishing(now):
    global result
    close = N+1
    fishing_shark = []
    for _ in range(len(shark)):
        n, m, s, d, b = shark.popleft()
        if n == now and m < close:
            if fishing_shark:
                shark.append(fishing_shark.pop())
            fishing_shark.append(n, m, s, d, b)
        else:
            shark.append(n, m, s, d, b)
    if fishing_shark:
        n, m, s, d, b = fishing_shark.pop()
        result += b


def move_shark(temp):
    for _ in range(shark):
        n, m, speed, dir, big = shark.popleft()
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
        shark.append((nn, nm, speed, dir, big))


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
    pass


result = 0
for i in range(1, M+1):
    fishing(i)
    temp = copy.deepcopy(arr)
    move_shark(temp)
    eat_shark()
print(result)
