# 저울
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 0
sum = 0
for i in range(N):
    if sum+1 >= arr[i]:
        sum += arr[i]
    else:
        result = sum+1
        break

if result == 0:
    result = sum+1

print(result)
