# 치킨 배달
from itertools import combinations

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken.append([i, j])

distance = int(1e9)
result = 0
final = []
for x in combinations(chicken, M):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                for ch in x:
                    temp = abs(i-ch[0]) + abs(j-ch[1])
                    distance = min(distance, temp)
                result += distance
                distance = int(1e9)
    final.append(result)
    result = 0

print(min(final))
