from itertools import permutations

N, M = map(int, input().split())
arr = []
for i in range(1, N+1):
    arr.append(i)

for x in permutations(arr, M):
    for y in x:
        print(y, end=' ')
    print()
