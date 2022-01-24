# 집합의 표현
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
N, m = map(int, input().split())
parent = [i for i in range(N+1)]


def union(x, y):
    a = find_parent(x)
    b = find_parent(y)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]


def is_set(x, y):
    if find_parent(x) == find_parent(y):
        print('YES')
    else:
        print('NO')


for _ in range(m):
    witch, a, b = map(int, input().split())
    if witch == 0:
        union(a, b)
    else:
        is_set(a, b)
