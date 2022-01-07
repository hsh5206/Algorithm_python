# 촌수계산

from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
x, y = map(int, input().split())
k = int(input())
arr = [[] for _ in range(N+1)]
for t in range(k):
    i, j = map(int, input().split())
    arr[i].append(j)
    arr[j].append(i)
visited = [False] * (N+1)
result = [-1] * (N+1)


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    result[start] = 0
    while q:
        x = q.popleft()
        for nx in arr[x]:
            if visited[nx] == False:
                visited[nx] = True
                result[nx] = result[x] + 1
                q.append(nx)


bfs(x)
print(result[y])
