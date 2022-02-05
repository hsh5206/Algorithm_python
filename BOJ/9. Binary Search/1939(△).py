# 중량제한
import sys
from collections import deque
MAX = sys.maxsize
input = sys.stdin.readline
N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]
weight = [MAX] * (N+1)
for _ in range(M):
    a, b, cost = map(int, input().split())
    arr[a].append((b, cost))
    arr[b].append((a, cost))
start_city, arrive_city = map(int, input().split())


def bfs(mid):
    q = deque()
    q.append(start_city)
    visited[start_city] = True
    while q:
        now = q.popleft()
        if now == arrive_city:
            return True
        for nnow, ncost in arr[now]:
            if not visited[nnow]:
                if mid <= ncost:
                    visited[nnow] = True
                    q.append(nnow)
    return False


result = 0
start, end = 1, int(1e9)
while start <= end:
    visited = [False] * (N+1)
    mid = (start+end) // 2
    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)
