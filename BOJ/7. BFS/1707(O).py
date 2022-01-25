# 이분 그래프
import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    global result
    q = deque()
    q.append(start)
    visited[start] = 0
    while q:
        node = q.popleft()
        for nnode in arr[node]:
            if visited[nnode] == -1:
                visited[nnode] = visited[node] % 2 + 1
                q.append(nnode)
            else:
                if visited[nnode] == visited[node]:
                    result = 'NO'
                    return


T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    visited = [-1] * (V+1)
    arr = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    result = 'YES'
    for i in range(1, len(visited)):
        if visited[i] == -1 and result == 'YES':
            bfs(i)
    print(result)
