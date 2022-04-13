# 로봇
import heapq
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[0]*(M+1)] + [[0]+list(map(int, input().split())) for _ in range(N)]
sa, sb, sd = map(int, input().split())
ea, eb, ed = map(int, input().split())


def dijkstra():
    q = []
    heapq.heappush(q, (0, sa, sb, sd))
    visited = [[[False] * (5) for _ in range(M+1)] for _ in range(N+1)]
    visited[sa][sb][sd] = True
    while q:
        dist, x, y, dir = heapq.heappop(q)
        if (x, y, dir) == (ea, eb, ed):
            return dist
        for type in ['Go', 'Turn']:
            nx, ny, ndir = x, y, dir
            if type == 'Go':
                for k in range(1, 4):
                    nx, ny, ndir = Go(x, y, dir, k)
                    if 0 < nx <= N and 0 < ny <= M and arr[nx][ny] == 0 and not visited[nx][ny][ndir]:
                        visited[nx][ny][ndir] = True
                        heapq.heappush(q, (dist+1, nx, ny, ndir))
                    else:
                        break
            elif type == 'Turn':
                for k in range(1, 5):
                    if dir != k and not visited[nx][ny][k]:
                        visited[nx][ny][k] = True
                        if (dir == 1 and k == 2) or (dir == 2 and k == 2) or (dir == 3 and k == 4) or (dir == 4 and k == 3):
                            heapq.heappush(q, (dist+2, nx, ny, k))
                        else:
                            heapq.heappush(q, (dist+1, nx, ny, k))


def Go(x, y, dir, num):
    if dir == 1:
        y += num
    elif dir == 2:
        y -= num
    elif dir == 3:
        x += num
    else:
        x -= num
    return x, y, dir


print(dijkstra())
