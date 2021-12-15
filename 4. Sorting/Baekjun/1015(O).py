# 수열정렬

N = int(input())
arr = list(map(int, input().split()))

temp = sorted(arr)

result = [0] * N
for i in range(N):
    for j in range(N):
        if temp[i] == arr[j]:
            result[j] = i
            arr[j] = -1
            break

for i in range(N):
    print(result[i], end=' ')
