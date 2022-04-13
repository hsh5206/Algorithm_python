# 로봇
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
sa, sb, sd = map(int, input().split())
ea, eb, ed = map(int, input().split())
dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]


def bfs():
    q = deque()
    q.append((0, sa-1, sb-1, sd))
    visited = [[[False for _ in range(5)] for _ in range(M)] for _ in range(N)]
    visited[sa-1][sb-1][sd] = True
    while q:
        dist, x, y, dir = q.popleft()
        if (x, y, dir) == (ea-1, eb-1, ed):
            return dist
        for type in ['Go', 'Turn']:
            nx, ny, ndir = x, y, dir
            if type == 'Go':
                for _ in range(3):
                    nx += dx[dir]
                    ny += dy[dir]
                    if 0 <= nx < N and 0 <= ny < M and visited[nx][ny][ndir]:
                        continue
                    if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0 and not visited[nx][ny][ndir]:
                        visited[nx][ny][ndir] = True
                        q.append((dist+1, nx, ny, ndir))
                    else:
                        break
            elif type == 'Turn':
                for k in range(1, 5):
                    if dir != k and not visited[nx][ny][k]:
                        visited[nx][ny][ndir] = True
                        if (dir == 1 and k == 2) or (dir == 2 and k == 2) or (dir == 3 and k == 4) or (dir == 4 and k == 3):
                            q.append((dist+2, nx, ny, k))
                        else:
                            q.append((dist+1, x, y, k))


print(bfs())
