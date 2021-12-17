# 국영수

N = int(input())
arr = []
for _ in range(N):
    a, b, c, d = input().split()
    arr.append((a, b, c, d))

arr.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for x in arr:
    print(x[0])
