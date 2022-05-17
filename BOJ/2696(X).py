# 중앙값 구하기
import heapq
import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N = int(input())
    left = []
    right = []
    arr = []
    if N % 10 == 0:
        for _ in range(N//10):
            arr += list(map(int, input().split()))
    else:
        for _ in range(N//10+1):
            arr += list(map(int, input().split()))

    mid = arr[0]
    result = [mid]
    for i, x in enumerate(arr[1:]):
        if x > mid:
            heapq.heappush(right, x)
        else:
            heapq.heappush(left, -x)
        if i % 2 == 0:
            if len(left) < len(right):
                heapq.heappush(left, -mid)
                mid = heapq.heappop(right)
            else:
                heapq.heappush(right, mid)
                mid = -heapq.heappop(left)
            result.append(mid)

    print(len(result))
    for i in range(len(result)):
        if i != 0 and i % 10 == 0:
            print()
        print(result[i], end=' ')
    print()
