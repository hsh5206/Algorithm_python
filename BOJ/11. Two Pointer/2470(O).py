# 두 용액

'''
산성 용액(+) & 알칼리성 용액(-)
두개를 뽑아서 합이 0에 가장 가깝게 하는 두 특성 값 출력
N => 2 ~ 100,000

2중 for문 X
'''
# -2, 4, -99, -1, 98
# -99, -2, -1, 4, 98
# -1, -2, 4, 98, -99

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = []
min_result = int(2*1e9+1)

sum = 0
left = 0
right = N-1
while left < right:
    sum = arr[left] + arr[right]
    if abs(sum) < min_result:
        min_result = abs(sum)
        result = [arr[left], arr[right]]
    if sum < 0:
        left += 1
    elif sum > 0:
        right -= 1
    else:
        break
    sum = 0

print(*result, sep=' ')
