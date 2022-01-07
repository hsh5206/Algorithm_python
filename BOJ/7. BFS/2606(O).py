# 바이러스
from collections import deque
N = int(input())
K = int(input())

arr = [[] for _ in range((N+1))]
for _ in range(K):
    a, b = map(int, input().split())
    arr[a].append((b))
    arr[b].append((a))

q = deque()
visited = [False]*(N+1)
parent = [0] * (N+1)

q.append((1))
visited[1] = True
while q:
    x = q.popleft()
    parent[x] = 1
    for i in arr[x]:
        if not visited[i]:
            q.append(i)
            visited[i] = True


result = 0
for x in parent:
    if x == 1:
        result += 1
print(result - 1)
