# 줄 세우기
from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
front = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    front[b] += 1


def sort():
    result = []
    q = deque()
    for k in range(1, len(front)):
        if front[k] == 0:
            q.append(k)
    while q:
        now = q.popleft()
        result.append(now)
        for nnow in arr[now]:
            front[nnow] -= 1
            if front[nnow] == 0:
                q.append(nnow)
    print(*result)


sort()
