# https://programmers.co.kr/learn/courses/30/lessons/81302

from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def solution(places):
    answer = []
    for room in places:
        answer.append(check(room))
    return answer


def check(room):
    person = []
    for i in range(5):
        for j in range(5):
            if room[i][j] == 'P':
                person.append((i, j))
    if not person:
        return 1
    return bfs(person, room)


def bfs(person, room):
    for i, j in person:
        q = deque()
        q.append((i, j))
        visited = [[0] * 5 for _ in range(5)]
        visited[i][j] = 1
        while q:
            x, y = q.popleft()
            if visited[x][y] == 3:
                continue
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                    if room[nx][ny] != 'X':
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
                    if room[nx][ny] == 'P':
                        return 0
    return 1


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
      "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
