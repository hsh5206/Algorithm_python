# 행렬

N, M = map(int, input().split())

a = []
b = []
for i in range(N):
    a.append(list(map(int, input())))
for i in range(N):
    b.append(list(map(int, input())))


def do(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            a[x][y] = 1 - a[x][y]


count = 0
for i in range(N-2):
    for j in range(M-2):
        if a[i][j] != b[i][j]:
            do(i, j)
            count += 1

for i in range(N):
    for j in range(M):
        if a[i][j] != b[i][j]:
            count = -1
            break

print(count)
