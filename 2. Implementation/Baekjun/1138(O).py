# 한 줄로 서기

N = int(input())
arr = list(map(int, input().split()))
result = [0] * N

for i in range(N):
    z_count = 0
    for j in range(N):
        if z_count == arr[i] and result[j] == 0:
            result[j] = i + 1
            break
        if result[j] == 0:
            z_count += 1

for x in result:
    print(x, end=' ')
