# 위에서 아래로
n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

arr = sorted(arr, reverse=True)

for i in arr:
    print(i, end=' ')
