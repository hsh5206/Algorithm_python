# 네트워크
from collections import deque


def solution(n, computers):
    parent = [i for i in range(n)]
    for i in range(n):
        bfs(i, parent, computers)
    parent = set(parent)
    return len(parent)


def bfs(start, parent, computers):
    q = deque()
    q.append(start)
    while q:
        node = q.popleft()
        for nnode in range(len(computers[node])):
            if node != nnode and computers[node][nnode] == 1:
                if parent[nnode] != parent[node]:
                    parent[nnode] = parent[node]
                    q.append(nnode)
