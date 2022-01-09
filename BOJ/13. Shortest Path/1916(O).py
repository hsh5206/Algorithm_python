# 최소비용 구하기

import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
dist = [INF] * (N+1)
for _ in range(M):
    a, b, cost = map(int, input().split())
    arr[a].append([cost, b])
X, Y = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    while q:
        cost, node = heapq.heappop(q)
        if cost > dist[node]:
            continue
        for edge in arr[node]:
            temp = edge[0] + cost
            if temp < dist[edge[1]]:
                dist[edge[1]] = temp
                heapq.heappush(q, [temp, edge[1]])


dijkstra(X)
print(dist[Y])
