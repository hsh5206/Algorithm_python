# 문제집
import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
front = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    front[b] += 1


def solve():
    result = []
    q = []
    for k in range(1, len(front)):
        if front[k] == 0:
            heapq.heappush(q, k)
    while q:
        now = heapq.heappop(q)
        result.append(now)
        for nnow in arr[now]:
            front[nnow] -= 1
            if front[nnow] == 0:
                heapq.heappush(q, nnow)
    print(*result)


solve()
