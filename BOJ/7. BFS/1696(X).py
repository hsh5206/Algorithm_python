# 숨바꼭질
from collections import deque


def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        if x == K:
            print(result[x])
            break
        for nx in (x - 1, x+1, x*2):
            if 0 <= nx <= MAX and not result[nx]:  # 해당 번호에 가본 적이 없으면
                result[nx] = result[x] + 1
                queue.append(nx)


N, K = map(int, input().split())
MAX = 10 ** 5
result = [0] * (MAX)  # 해당 번호까지 가는 최소 시간
bfs(N)
