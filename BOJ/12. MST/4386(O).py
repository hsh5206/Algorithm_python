# 별자리 만들기
import heapq
import sys
import math
input = sys.stdin.readline

N = int(input())
star = []
for _ in range(N):
    x, y = map(float, input().split())
    star.append((x, y))

arr = [[]for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        x, y = star[i][0], star[i][1]
        nx, ny = star[j][0], star[j][1]
        dist = math.sqrt(abs(x-nx)**2+abs(y-ny)**2)
        arr[i].append((dist, j))

result = 0
visited = [False] * N


def prim(start):
    global result
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)
        if not visited[node]:
            result += dist
            visited[node] = True
        for ndist, nnode in arr[node]:
            if not visited[nnode]:
                heapq.heappush(q, (ndist, nnode))


prim(0)
print(f'{result:.2f}')
