# 지름길

import sys
input = sys.stdin.readline

N, D = map(int, input().split())
arr = [[] for _ in range(10001)]
dist = [i for i in range(D+1)]
for _ in range(N):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))

for i in range(D+1):
    if i != 0:
        dist[i] = min(dist[i], dist[i-1]+1)
    for x in arr[i]:
        if x[0] <= D and dist[x[0]] > x[1] + dist[i]:
            dist[x[0]] = x[1] + dist[i]

print(dist[D])
