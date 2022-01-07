# 전보
# 다익스트라 알고리즘
'''
3 2 1
1 2 4
1 3 2
'''

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, M, C = map(int, input().split())
graph = [[] for _ in range(N+1)]
dist = [INF] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start = C


def dijkstra(start):
    q = []
    dist[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        distance, now = heapq.heappop(q)
        if dist[now] < distance:
            continue
        for i in graph[now]:
            cost = distance + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

num = 0
max_time = 0
for i in range(1, N+1):
    if dist[i] != INF:
        num += 1
        max_time = max(max_time, dist[i])

print(dist)
print(num - 1, max_time)
