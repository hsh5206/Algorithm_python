# 드래곤 커브

from collections import deque
import sys
import copy
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    x, y, dir, g = map(int, input().split())
    q = deque()
    q.append((x, y, dir, g))
arr = [[0]*101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def dragon_curve(x, y, dir, g):
    while q:
        x, y, dir, g = q.popleft()
        arr[x][y] = 1
