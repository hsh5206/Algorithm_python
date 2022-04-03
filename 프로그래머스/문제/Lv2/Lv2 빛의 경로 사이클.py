# https://programmers.co.kr/learn/courses/30/lessons/86052

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def solution(grid):
    global answer, visited
    global N, M
    answer = []
    N = len(grid)
    M = len(grid[0])
    visited = [[[False]*4 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            for k in range(4):
                if not visited[i][j][k]:
                    light(i, j, k, grid)

    return sorted(answer)


def light(x, y, k, grid):
    global answer
    nx, ny, dir = x, y, k
    num = 0
    visited[x][y][k] = True
    while True:
        if grid[nx][ny] == 'R':
            dir = (dir+1) % 4
        elif grid[nx][ny] == 'L':
            dir = (dir-1) % 4

        nx = (nx + dx[dir]) % N
        ny = (ny + dy[dir]) % M
        num += 1

        if visited[nx][ny][dir]:
            if nx == x and ny == y and dir == k:
                answer.append(num)
                return

        visited[nx][ny][dir] = True
