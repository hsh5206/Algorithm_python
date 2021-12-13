# 팀 결성
# 서로소 집합 알고리즘

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    a = find(x)
    b = find(y)
    if a < b:
        b = a
    else:
        a = b


for _ in range(M):
    do, a, b = map(int, input().split())
    if do == 0:
        union(a, b)
    else:
        if parent[a] == parent[b]:
            print("YES")
        else:
            print("NO")
