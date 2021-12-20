from itertools import combinations

N, M = map(int, input().split())
arr = []
for i in range(1, N+1):
    arr.append(i)

for x in combinations(arr, M):
    for i in range(len(x)):
        print(x[i], end=' ')
    print()
