# 치킨배달
'''
순열&조합 사용하기 itertools라이브러리
'''
from itertools import combinations

N, M = map(int, input().split())
loc = [list(map(int, input().split())) for _ in range(N)]

# 하우스와 치킨 좌표
chicken = []
house = []
for i in range(N):
    for j in range(N):
        if loc[i][j] == 1:
            house.append((i, j))
        elif loc[i][j] == 2:
            chicken.append((i, j))


# 치킨집 중에 M개 고르기 (조합) -> 리스트로 모든 경우의수
pick_chicken = list(combinations(chicken, M))
result = [0] * len(pick_chicken)

for i in house:
    for j in range(len(pick_chicken)):
        a = 1e9
        for k in pick_chicken[j]:
            temp = abs(i[0]-k[0])+abs(i[1]-k[1])
            a = min(a, temp)
        result[j] += a

print(min(result))
