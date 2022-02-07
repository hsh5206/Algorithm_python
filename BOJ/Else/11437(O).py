# LCA
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def make_depth(node, dep):
    visited[node] = True
    depth[node] = dep
    for nnode in arr[node]:
        if not visited[nnode]:
            parent[nnode] = node
            make_depth(nnode, dep+1)


def lca(x, y):
    if depth[x] > depth[y]:
        y, x = x, y
    while True:
        if depth[x] == depth[y]:
            break
        y = parent[y]
    for _ in range(depth[x]):
        if x == y:
            return x
        x = parent[x]
        y = parent[y]
    return x


N = int(input())
arr = [[]for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

parent = [i for i in range(N+1)]
depth = [0] * (N+1)
visited = [False] * (N+1)
make_depth(1, 0)


T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    print(lca(x, y))
