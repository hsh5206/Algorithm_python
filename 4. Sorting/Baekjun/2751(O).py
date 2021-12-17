# 수 정렬하기 2

N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

for x in sorted(arr):
    print(x)
