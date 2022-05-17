# 컬러볼
from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
balls = []
for i in range(N):
    color, big = map(int, input().split())
    balls.append((i, color, big))
balls.sort(key=lambda x: x[2])

answer = defaultdict(int)
prefix_sum = defaultdict(int)

result = 0
i, j = 0, 0
for i in range(N):
    while balls[j][2] < balls[i][2]:
        result += balls[i][j]
        prefix_sum[balls[j][1]] += balls[j][2]
        j += 1
    answer[balls[i][0]] = result - prefix_sum[balls[i][1]]


print(*answer, sep='\n')
