# 도시 분할 계획
# 최소 신장 트리 - 크루스칼 알고리즘

N, M = map(int, input().split())
INF = int(1e9)
edges = []
parent = [i for i in range(N + 1)]
for i in range(N + 1):
    parent[i] = i
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    a = find(x)
    b = find(y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


result = 0
expensive = 0
edges.sort()
for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        result += cost
        expensive = cost

print(result - expensive)
