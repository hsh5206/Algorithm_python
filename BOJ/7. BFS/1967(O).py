# 트리의 지름
from collections import deque
import sys
input = sys.stdin.readline

V = int(input())
arr = [[] for _ in range(V+1)]
for _ in range(V):
    temp = list(map(int, input().split()))
    v = temp[0]
    for i in range(1, len(temp)-2, 2):
        arr[v].append((temp[i], temp[i+1]))
far_node = 0


def find(a, c):
    global far_node
    q = deque()
    q.append((a, c))
    visited = [False] * (V+1)
    visited[a] = True
    result = 0
    while q:
        node, cost = q.popleft()
        if result < cost:
            result = cost
            far_node = node
        for nnode, ncost in arr[node]:
            if not visited[nnode]:
                visited[nnode] = True
                q.append((nnode, cost+ncost))
    return result


find(1, 0)
print(find(far_node, 0))
