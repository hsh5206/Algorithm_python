# 최소 스패닝 트리

import sys
import heapq
input = sys.stdin.readline
V, E = map(int, input().split())
arr = [[] for _ in range(V+1)]
chk = [False] * (V+1)
for _ in range(E):
    a, b, c = map(int, input().split())
    arr[a].append([c, b])
    arr[b].append([c, a])

heap = [(0, 1)]

result = 0
while heap:
    cost, node = heapq.heappop(heap)
    if chk[node] == False:
        chk[node] = True
        result += cost
        for next_edge in arr[node]:
            if chk[next_edge[1]] == False:
                heapq.heappush(heap, next_edge)

print(result)
