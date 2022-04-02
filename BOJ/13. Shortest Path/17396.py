# 백도어
import heapq
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
cant_go = list(map(int, input().split()))
cant_go[-1] = 0
arr = [[]for _ in range(N)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    arr[a].append((cost, b))
    arr[b].append((cost, a))
dist = [sys.maxsize] * N


def dijkstra():
    q = []
    heapq.heappush(q, (0, 0))
    dist[0] = 0
    while q:
        cost, node = heapq.heappop(q)
        if dist[node] < cost:
            continue
        for ncost, nnode in arr[node]:
            if not cant_go[nnode] and dist[nnode] > cost+ncost:
                dist[nnode] = cost+ncost
                heapq.heappush(q, (cost+ncost, nnode))


dijkstra()
print(-1) if dist[N-1] == sys.maxsize else print(dist[N-1])
