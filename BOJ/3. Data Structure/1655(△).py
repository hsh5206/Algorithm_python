# 가운데를 말해요
import sys
import heapq
input = sys.stdin.readline

N = int(input())
left = []
right = []
for _ in range(N):
    if len(left) == len(right):
        heapq.heappush(left, -int(input()))
    else:
        heapq.heappush(right, int(input()))
    if len(left) != 0 and len(right) != 0 and -left[0] > right[0]:
        add_left = heapq.heappop(right)
        add_right = heapq.heappop(left)
        heapq.heappush(left, -add_left)
        heapq.heappush(right, -add_right)
    print(-left[0])
