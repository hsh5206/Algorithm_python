# 특정 거리의 도시 찾기

import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

N, M, K, start = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

num = []
for i in range(len(distance)):
    if distance[i] == K:
        num.append(i)

if len(num) == 0:
    print(-1)
else:
    for i in range(len(num)):
        print(num[i])
