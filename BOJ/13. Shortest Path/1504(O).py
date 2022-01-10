# 특정한 최단 경로

import sys
import heapq
import copy
INF = sys.maxsize
input = sys.stdin.readline
N, E = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, cost = map(int, input().split())
    arr[a].append([cost, b])
    arr[b].append([cost, a])
result = [INF] * (N+1)
middle = [[] for _ in range(2)]
real = list(map(int, input().split()))
temp = copy.deepcopy(real)
middle[0] = temp
middle[0].reverse()
middle[0].append(1)
middle[0].reverse()
middle[0].append(N)
middle[1] = real
middle[1].append(1)
middle[1].reverse()
middle[1].append(N)


def dijkstra(start, end, result):
    q = []
    heapq.heappush(q, (0, start))
    result[start] = 0
    while q:
        cost, node = heapq.heappop(q)
        for ncost, nnode in arr[node]:
            if cost > result[nnode]:
                continue
            temp = cost + ncost
            if result[nnode] > temp:
                result[nnode] = temp
                heapq.heappush(q, [temp, nnode])
    return result[end]


minimum = INF
for middle in middle:
    value = 0
    for i in range(len(middle)-1):
        temp_result = copy.deepcopy(result)
        value += dijkstra(middle[i], middle[i+1], temp_result)
    minimum = min(minimum, value)

if minimum >= INF:
    print(-1)
else:
    print(minimum)
