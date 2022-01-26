# 드래곤 커브
import sys
input = sys.stdin.readline
T = int(input())
arr = [[False] * 101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

q = []
for _ in range(T):
    y, x, d, g = map(int, input().split())
    q.append((x, y, d, g))


def dragon_curve():
    for x, y, d, g in q:
        arr[x][y] = True
        dir = [d]
        for _ in range(g):
            for d in range(len(dir)-1, -1, -1):
                temp = (dir[d] + 1) % 4
                dir.append(temp)
        for d in dir:
            x += dx[d]
            y += dy[d]
            if 0 <= x < 101 and 0 <= y < 101:
                arr[x][y] = True


dragon_curve()

result = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i + 1][j] and arr[i][j + 1] and arr[i + 1][j + 1]:
            result += 1
print(result)
