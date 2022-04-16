# 횡단보도
import heapq
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append((i, b))
    arr[b].append((i, a))


def dijkstra():
    q = []
    heapq.heappush(q, (0, 1))
    visited = [sys.maxsize for _ in range(N+1)]
    visited[1] = 0
    while q:
        time, node = heapq.heappop(q)
        if visited[node] < time:
            continue
        for i, nnode in arr[node]:
            ntime = i+((time-i)//M)*M if (time-i) % M == 0 else i + \
                ((time-i)//M+1)*M
            if time <= ntime and visited[nnode] > ntime+1:
                visited[nnode] = ntime+1
                heapq.heappush(q, (ntime+1, nnode))
    return visited[N]


print(dijkstra())

# i+(n-1)M
# time <= i+(n-1)M
# (time-i)/M <= n-1
# time == 15, i == 2, M == 3, 3+6+6, 3+(13//1)*1
