# 연결 요소의 개수
# BFS & 서로소 집합

from collections import deque
N, M = map(int, input().split())

visited = [False]*(N+1)

arr = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        x = q.popleft()
        for i in arr[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        cnt += 1
print(cnt)
