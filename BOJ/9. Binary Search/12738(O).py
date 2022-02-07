# 가장 긴 증가하는 부분 수열 3
import sys
import bisect
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))

result = [arr[0]]

for i in range(1, N):
    if arr[i] > result[-1]:
        result.append(arr[i])
    else:
        index = bisect.bisect_left(result, arr[i])
        result[index] = arr[i]

print(len(result))
