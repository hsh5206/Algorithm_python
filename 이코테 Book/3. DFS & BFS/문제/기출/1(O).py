# 특정 거리의 도시 찾기
# BFS

import sys
from collections import deque
input = sys.stdin.readline

N, M, K, start = map(int, input().split())
maps = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    maps[a].append(b)

distance = [int(1e9)] * (N + 1)


def dijkstra(start):
    q = deque()
    q.append(start)
    distance[start] = 0
    while q:
        now = q.popleft()
        for temp in maps[now]:
            cost = distance[now] + 1
            if cost < distance[temp]:
                distance[temp] = cost
                q.append(temp)


dijkstra(start)

flag = -1
for i in range(len(distance)):
    if distance[i] == K:
        flag = 1
        print(i)

if flag == -1:
    print(flag)
