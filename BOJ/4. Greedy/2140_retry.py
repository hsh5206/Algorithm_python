# 지뢰찾기
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(input()))

dx = [0, 0, 1, -1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

for i in range(N):
    for j in range(N):
        for k in range(8):
            pass
