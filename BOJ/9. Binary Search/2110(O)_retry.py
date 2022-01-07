# 공유기 설치

import sys

N, C = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort()
start, end = 1, arr[-1] - arr[0]


def binarySearch(dist):
    # 첫집에 공유기 설치
    count = 1
    house = arr[0]
    for i in range(1, N):
        if house + dist <= arr[i]:
            count += 1
            house = arr[i]
    return count


result = 0
while start <= end:
    mid = (start+end)//2
    if binarySearch(mid) >= C:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
