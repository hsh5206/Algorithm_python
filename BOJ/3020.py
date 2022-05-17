# 개똥벌레
import sys
input = sys.stdin.readline
N, H = map(int, input().split())


def get_break(h, arr):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] <= h:
            left = mid + 1
        else:
            right = mid - 1
    return len(arr) - (right+1)


arr1 = []
arr2 = []
for i in range(N):
    if i % 2 == 0:
        arr1.append(int(input()))
    else:
        arr2.append(int(input()))
arr1.sort()
arr2.sort()

answer = [sys.maxsize, 0]
for i in range(1, H+1):
    cnt1 = get_break(i-1, arr1)
    cnt2 = get_break(H-i, arr2)
    if cnt1+cnt2 < answer[0]:
        answer = [cnt1+cnt1, 1]
    elif cnt1+cnt2 == answer[0]:
        answer[1] += 1
print(*answer)
