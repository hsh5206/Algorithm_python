# 트리의 지름
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
N = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, cost = map(int, input().split())
    arr[a].append([b, cost])
    arr[b].append([a, cost])
result = []


def dfs(start, c):
    global result
    all_cost = c
    visited[start] = True
    for node, cost in arr[start]:
        if not visited[node]:
            all_cost += cost
            dfs(node, all_cost)
            all_cost -= cost
    result.append([all_cost, start])


visited = [False] * (N+1)
dfs(1, 0)
result.sort()
temp, node = result.pop()
visited = [False] * (N+1)
result = []
dfs(node, 0)
result.sort()
cost, temp = result.pop()
print(cost)
