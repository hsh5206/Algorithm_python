# 그대, 그머가 되어
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

a, b = map(int, input().split())
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
dist = [INF] * (N+1)
for i in range(M):
    x, y = map(int, input().split())
    graph[x].append((y, 1))
    graph[y].append((x, 1))


def dijkstra(start):
    q = []
    dist[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        distance, now = heapq.heappop(q)
        if distance > dist[now]:
            continue
        for i in graph[now]:
            cost = distance + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(a)
if dist[b] == INF:
    print(-1)
else:
    print(dist[b])
