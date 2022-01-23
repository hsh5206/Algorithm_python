# 알파벳
import sys
input = sys.stdin.readline
R, C = map(int, input().split())
arr = []
for _ in range(R):
    arr.append(list(input().strip()))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
result = 0


def move():
    global result
    q = set([(0, 0, arr[0][0])])
    while q:
        x, y, hist = q.pop()
        result = max(result, len(hist))
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < R and 0 <= ny < C:
                if arr[nx][ny] not in hist:
                    q.add((nx, ny, hist+arr[nx][ny]))


move()
print(result)
