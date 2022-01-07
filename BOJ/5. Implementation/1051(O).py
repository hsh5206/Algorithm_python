# 숫자 정사각형

N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input())))

max_value = -1
temp = 0
for i in range(N):
    for j in range(M):
        for k in range(j+1, M):
            if arr[i][j] == arr[i][k]:
                temp = k - j + 1
                if 0 <= i + temp - 1 < N:
                    if arr[i][j] == arr[i + temp - 1][j]:
                        if arr[i][j] == arr[i + temp - 1][k]:
                            max_value = max(max_value, temp)

print(max_value**2)
