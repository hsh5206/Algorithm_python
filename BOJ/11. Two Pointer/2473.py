# 세 용액
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = sys.maxsize
three = []
for i in range(N-2):
    left = i+1
    right = N-1
    while left < right:
        temp = arr[i] + arr[left] + arr[right]
        if abs(temp) < result:
            result = abs(temp)
            three = [arr[i], arr[left], arr[right]]
        if temp < 0:
            left += 1
        elif temp > 0:
            right -= 1
        else:
            break

print(*three)
