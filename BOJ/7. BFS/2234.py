# 성곽
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
M, N = map(int, input().split())
arr = []
check = 15
for _ in range(N):
    arr.append(list(map(int, input().split())))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(a, b, arr, visited, room_num):
    q = deque()
    q.append((a, b))
    visited[a][b] = room_num
    result = 1
    while q:
        x, y = q.popleft()
        info = bin(arr[x][y] & check)[2:]
        info = '0'*(4-len(info))+info
        for k, bit in enumerate(info):
            if bit == '0':
                nx = x + dx[k]
                ny = y + dy[k]
                if not visited[nx][ny]:
                    visited[nx][ny] = room_num
                    q.append((nx, ny))
                    result += 1
            if bit == '1':
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < M and visited[nx][ny]:
                    room_dict[visited[nx][ny]].add(room_num)
                    room_dict[room_num].add(visited[nx][ny])
    return result


visited = [[0 for _ in range(M)] for _ in range(N)]
room_count = 0
room_dict = defaultdict(set)
room_info = defaultdict(int)
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            room_count += 1
            size = bfs(i, j, arr, visited, room_count)
            room_info[room_count] = size

break_max = 0
for a in room_dict:
    for b in room_dict[a]:
        if a != b:
            break_max = max(break_max, room_info[a]+room_info[b])
print(room_count, max(room_info.values()), break_max)
