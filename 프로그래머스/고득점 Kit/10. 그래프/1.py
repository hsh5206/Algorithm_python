# 가장 먼 노드
import sys
MAX = sys.maxsize


def solution(n, edge):
    arr = [[] for _ in range(n+1)]
    for x, y in edge:
        arr[x].append(y)
        arr[y].append(x)
    return go(n, arr)


def go(n, arr):
    visited = [MAX] * (n+1)
    visited[0], visited[1] = 0, 1
    q = []
    q.append(1)
    while q:
        node = q.pop()
        for nnode in arr[node]:
            if visited[nnode] > visited[node] + 1:
                q.append(nnode)
                visited[nnode] = visited[node] + 1
    result = 0
    max_value = max(visited)
    for x in visited:
        if x == max_value:
            result += 1
    return result
