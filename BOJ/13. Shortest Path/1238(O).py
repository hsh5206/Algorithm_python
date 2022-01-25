# 파티
import sys
import heapq
input = sys.stdin.readline
MAX = sys.maxsize
N, M, X = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    arr[a].append((cost, b))

come = [MAX] * (N+1)
go = [MAX] * (N+1)


def go_dijkstra(x):
    q = []
    heapq.heappush(q, (0, x))
    go[x] = 0
    while q:
        cost, node = heapq.heappop(q)
        for ncost, nnode in arr[node]:
            if go[nnode] > ncost + go[node]:
                go[nnode] = ncost + go[node]
                heapq.heappush(q, (ncost, nnode))


def come_dijkstra(x):
    temp = [MAX] * (N+1)
    q = []
    heapq.heappush(q, (0, x))
    temp[x] = 0
    while q:
        cost, node = heapq.heappop(q)
        for ncost, nnode in arr[node]:
            if temp[nnode] > ncost + temp[node]:
                temp[nnode] = ncost + temp[node]
                heapq.heappush(q, (ncost, nnode))
    return temp[X]


go_dijkstra(X)
for i in range(1, N+1):
    come[i] = come_dijkstra(i)

result = [0] * (N+1)
for i in range(1, N+1):
    result[i] = come[i]+go[i]
print(max(result))
