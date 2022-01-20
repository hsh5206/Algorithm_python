# 숨바꼭질 4
import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
visited = [0] * 100001
path = [0] * 100001


def move():
    q = deque()
    q.append(N)
    while q:
        now = q.popleft()
        if now == K:
            result = deque()
            while now != N:
                result.appendleft(now)
                now = path[now]
            result.appendleft(now)
            return result
        for nnow in [now-1, now+1, now*2]:
            if 0 <= nnow <= 100000 and visited[nnow] == 0:
                visited[nnow] = visited[now] + 1
                path[nnow] = now
                q.append(nnow)


result = move()
print(visited[K])
print(*result, sep=' ')
