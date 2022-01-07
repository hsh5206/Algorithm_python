# 최단 경로

import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))

heap = [(0, start)]
distance[start] = 0

while heap:
    cost, node = heapq.heappop(heap)
    if distance[node] < cost:
        continue
    for ncost, nnode in graph[node]:
        if distance[nnode] > cost + ncost:
            distance[nnode] = cost + ncost
            heapq.heappush(heap, (distance[nnode], nnode))

for x in range(1, len(distance)):
    if distance[x] == INF:
        print("INF")
    else:
        print(distance[x])
