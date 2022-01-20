# 도시 분할 계획
import heapq
import sys
input = sys.stdin.readline


def mst():
    q = []
    heapq.heappush(q, (0, 1))
    while q:
        cost, house = heapq.heappop(q)
        if not conneted[house]:
            conneted[house] = True
            total.append(cost)
            for ncost, nhouse in arr[house]:
                if not conneted[nhouse]:
                    heapq.heappush(q, (ncost, nhouse))


N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    arr[a].append((cost, b))
    arr[b].append((cost, a))
conneted = [False] * (N+1)
total = []

mst()

max_value = max(total)
result = sum(total) - max_value
print(result)
