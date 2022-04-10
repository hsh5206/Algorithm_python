# 과제
import heapq
from collections import defaultdict
N = int(input())

arr = defaultdict(list)
for _ in range(N):
    dday, score = map(int, input().split())
    arr[dday].append(score)

q = []
answer = 0
now = max(arr.keys())
while 0 <= now:
    if q:
        score = heapq.heappop(q)
        score = -score
        answer += score
    for x in arr[now]:
        heapq.heappush(q, -x)
    now -= 1

print(answer)
