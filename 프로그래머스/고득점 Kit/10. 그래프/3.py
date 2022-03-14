# 방의 개수
from collections import deque
from collections import defaultdict as dfd
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def solution(arrows):
    start = (0, 0)
    visited = dfd(bool)
    lines = dfd(bool)
    q = deque()
    q.append(start)
    for k in arrows:
        x, y = start
        nx, ny = x, y
        for _ in range(2):
            nx += dx[k]
            ny += dy[k]
            start = (nx, ny)
            q.append(start)

    answer = 0
    node = q.popleft()
    visited[node] = True
    while q:
        nnode = q.popleft()
        if visited[nnode]:
            if not lines[(node, nnode)]:
                answer += 1
        else:
            visited[nnode] = True
        lines[(node, nnode)] = True
        lines[(nnode, node)] = True
        node = nnode
    return answer
