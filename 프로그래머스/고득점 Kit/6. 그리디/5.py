# 섬 연결하기
import heapq


def solution(n, costs):
    arr = [[]for _ in range(n)]
    for x, y, cost in costs:
        arr[x].append((cost, y))
        arr[y].append((cost, x))
    answer = prim(n, arr, 0)
    return answer


def prim(n, arr, start):
    result = 0
    visited = [False] * n
    q = []
    heapq.heappush(q, (0, start))
    while q:
        cost, node = heapq.heappop(q)
        if not visited[node]:
            visited[node] = True
            result += cost
        for ncost, nnode in arr[node]:
            if not visited[nnode]:
                heapq.heappush(q, (ncost, nnode))
    return result
