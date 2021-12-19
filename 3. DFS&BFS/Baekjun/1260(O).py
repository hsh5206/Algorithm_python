# DFS와 BFS

import sys
from collections import deque
input = sys.stdin.readline
N, M, start = map(int, input().split())

arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [False] * (N+1)

for i in range(1, N+1):
    arr[i].sort()


def dfs(start):
    print(start, end=' ')
    visited[start] = True
    for i in range(len(arr[start])):
        if visited[arr[start][i]] == False:
            dfs(arr[start][i])


def bfs(start):
    visited[start] = True
    q = deque()
    q.append(start)
    while q:
        x = q.popleft()
        visited[x] = True
        print(x, end=' ')
        for i in range(len(arr[x])):
            if visited[arr[x][i]] == False and arr[x][i] not in q:
                q.append(arr[x][i])


dfs(start)
visited = [False] * (N+1)
print()
bfs(start)
