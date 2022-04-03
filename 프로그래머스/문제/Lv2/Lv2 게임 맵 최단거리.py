# https://programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def solution(maps):
    global N, M
    N = len(maps)+1
    M = len(maps[0])+1
    maps = [[0]*(len(maps[0]))]+[[0]+map for map in maps]

    bfs(maps)
    return bfs(maps)


def bfs(maps):
    q = deque()
    q.append((1, 1))
    visited = [[0] * M for _ in range(N)]
    visited[1][1] = 1
    while q:
        x, y = q.popleft()
        if (x, y) == (N-1, M-1):
            return visited[x][y]
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 1 <= nx < N and 1 <= ny < M and maps[nx][ny] == 1:
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y]+1
                    q.append((nx, ny))
    return -1
