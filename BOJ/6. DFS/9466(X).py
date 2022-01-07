# 텀 프로젝트

import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
sys.setrecursionlimit(111111)


for _ in range(T):
    N = int(input())
    arr = deque(map(int, input().split()))
    arr.appendleft(0)

    result = 0
    depth = 1

    def dfs(start, to):
        global result
        if start == to:
            return depth
        if to == arr[to]:
            return
        if start == arr[to]:
            arr[start] = start
            return depth
        else:
            depth += 1
            dfs(start, arr[to])

    for i in range(1, N+1):
        dfs(i, arr[i])

    if depth == 1:
        depth = 0
    print(N - depth)
