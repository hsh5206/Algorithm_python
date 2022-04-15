# 성싶당 밀키트
import sys
from collections import defaultdict
input = sys.stdin.readline
N, G, K = map(int, input().split())
info = defaultdict(list)
for _ in range(N):
    speed, limit, isImportant = map(int, input().split())
    info[isImportant].append((speed, limit))


def get_g(x, k):
    result = 0
    for speed, limit in info[0]:
        result += speed*max(1, x-limit)
    info[1].sort(key=lambda k: -k[0]*max(1, x-k[1]))
    for t in range(k, len(info[1])):
        speed, limit = info[1][t]
        result += speed*max(1, x-limit)
    return result


result = 0
left, right = 0, int(2e9)
while left <= right:
    mid = (left+right)//2
    g = get_g(mid, K)
    if g <= G:
        result = mid
        left = mid + 1
    else:
        right = mid - 1
print(result)
