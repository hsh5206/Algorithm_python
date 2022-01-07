# 네트워크 연결

'''
아이디어
1번 노드에서 시작해서 연결된 간선들 중 최소값을 포함
부분 트리에 연결된 간선들 중 최소값을 포함 (heapq)

시간복잡도
노드 수 N : 1000
간선 수 M : 100000
NlogM = 1000 * 100 = 1000000 (ok)

자료구조
q(heapq)
간선리스트(인접리스트)
visited[]
'''

import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    a, b, cost = map(int, input().split())
    arr[a].append([cost, b])
    arr[b].append([cost, a])


q = []
heapq.heappush(q, (0, 1))
result = 0
while q:
    cost, node = heapq.heappop(q)
    if not visited[node]:
        result += cost
        visited[node] = True
        for nnode in arr[node]:
            heapq.heappush(q, nnode)

print(result)
