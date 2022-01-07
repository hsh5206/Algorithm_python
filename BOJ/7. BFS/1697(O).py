# 숨바꼭질

from collections import deque
N, K = map(int, input().split())
MAX = int(1e5)
# 리스트에 걸린 시간을 넣어줄 거임
seconds = [0] * (MAX + 1)


def bfs(start):
    q = deque()
    q.append(start)
    while q:
        x = q.popleft()
        if x == K:
            print(seconds[x])
            break
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and not seconds[nx]:  # 처음 초기화 하는 것이면
                seconds[nx] = seconds[x] + 1
                q.append(nx)


bfs(N)
