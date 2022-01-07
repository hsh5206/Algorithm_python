# 스타트 링크

import sys
from collections import deque
input = sys.stdin.readline

total, now, final, U, D = map(int, input().split())
arr = [0] * (total+1)
D = -D
how = [U, D]


def bfs():
    q = deque()
    q.append(now)
    arr[now] = 1
    while q:
        x = q.popleft()
        for k in range(2):
            nx = x + how[k]
            if 0 < nx <= total:
                if arr[nx] == 0:
                    arr[nx] = arr[x] + 1
                    q.append(nx)


bfs()
result = arr[final] - 1
if result == -1:
    print("use the stairs")
else:
    print(result)
