# 숨바꼭질 3

from collections import deque


def bfs():
    q = deque()
    q.append(N)
    while q:
        now = q.popleft()
        if now == M:
            return visited[now]
        for k in [now-1, now+1, now*2]:
            nnow = k
            if 0 <= nnow < 1000001 and visited[nnow] == 0:
                if nnow == now*2 and now != 0:
                    visited[nnow] = visited[now]
                    q.appendleft(nnow)
                else:
                    visited[nnow] = visited[now] + 1
                    q.append(nnow)


N, M = map(int, input().split())
visited = [0] * 1000001
print(bfs())
