# https://programmers.co.kr/learn/courses/30/lessons/12978

import heapq
import sys


def solution(N, road, K):
    answer = 0
    arr = [[]for _ in range(N+1)]
    for a, b, time in road:
        arr[a].append((time, b))
        arr[b].append((time, a))
    visited = [sys.maxsize] * (N+1)
    dijkstra(arr, visited)

    return len([x for x in visited if x <= K])


def dijkstra(arr, visited):
    q = []
    heapq.heappush(q, (0, 1))
    visited[1] = 0
    while q:
        cost, node = heapq.heappop(q)
        if visited[node] > cost:
            continue
        for ncost, nnode in arr[node]:
            temp = cost + ncost
            if visited[nnode] > temp:
                visited[nnode] = temp
                heapq.heappush(q, (temp, nnode))
