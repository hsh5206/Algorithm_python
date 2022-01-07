# 체스판 다시 칠하기

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(input())


def paint(temp):
    countW = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if temp[i][j] == 'B':
                    countW += 1
            else:
                if temp[i][j] == 'W':
                    countW += 1
    countB = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if temp[i][j] == 'W':
                    countB += 1
            else:
                if temp[i][j] == 'B':
                    countB += 1
    return(min(countW, countB))


min_value = int(1e9)
for j in range(M - 7):
    temp = []
    for i in range(8):
        temp.append(arr[i][j:j+8])
    result = paint(temp)
    min_value = min(min_value, result)

temp = []
for k in range(N - 7):
    temp.append(arr[k:k+8])
    for j in range(M - 7):
        real = []
        for i in range(8):
            real.append(temp[k][i][j:j+8])
result = paint(real)
min_value = min(min_value, result)

print(min_value)
