# 친구 네트워크

import sys
input = sys.stdin.readline
T = int(input())


def find_parent(x):
    global result
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    global result
    x = find_parent(arr[a])
    y = find_parent(arr[b])
    if x < y:
        parent[y] = x
        num[x] += num[y]
    elif x > y:
        parent[x] = y
        num[y] += num[x]


for _ in range(T):
    N = int(input())
    arr = dict()
    n = 0
    parent = [i for i in range(2*N)]
    num = [1] * (2*N)
    for i in range(N):
        a, b = input().split()
        if a not in arr:
            arr[a] = n
            n += 1
        if b not in arr:
            arr[b] = n
            n += 1
        union(a, b)
        print(num[find_parent(arr[a])])
