# 연결 요소의 개수
# BFS & 서로소 집합

import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False] * (N+1)


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        x = q.popleft()
        for k in arr[x]:
            if visited[k] == False:
                q.append(k)
                visited[k] = True


count = 0
for i in range(1, N+1):
    if visited[i] == False:
        bfs(i)
        count += 1

print(count)
