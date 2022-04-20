# 두 동전
import copy
from collections import deque
N, M = map(int, input().split())
arr = []
money = deque()
for i in range(N):
    arr.append(list(input().strip()))
    for j in range(M):
        if arr[i][j] == 'o':
            money.append((i, j))
            arr[i][j] = '.'

visited = set()
visited.add(''.join(map(str, money)))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs():
    q = deque()
    q.append((0, money))
    while q:
        cnt, now = q.popleft()
        if cnt >= 10:
            return -1
        for k in range(4):
            # now를 깊은 복사
            temp = copy.deepcopy(now)
            # 동전의 개수는 두개
            for _ in range(2):
                x, y = temp.popleft()
                nx = x+dx[k]
                ny = y+dy[k]
                if 0 <= nx < N and 0 <= ny < M:
                    # . => 변한 값 append
                    if arr[nx][ny] == '.':
                        temp.append((nx, ny))
                    # # => 기존 값 append
                    elif arr[nx][ny] == '#':
                        temp.append((x, y))
            # 동전 개수가 1개이면 종료
            if len(temp) == 1:
                return cnt+1
            # 동전 개수가 0개이면 continue
            elif not temp:
                continue
            # 동전 개수가 2개이면 visited추가 & q.append
            visit = ''.join(map(str, temp))
            if visit not in visited:
                visited.add(visit)
                q.append((cnt+1, temp))
    return -1


print(bfs())
