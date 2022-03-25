# 입국심사
# https://www.acmicpc.net/problem/3079

import sys
input = sys.stdin.readline
N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))

annswer = 0
left, right = 0, max(arr)*M
while left <= right:
    mid = (left+right)//2
    people = 0
    for time in arr:
        people += mid//time
        if people > M:
            break
    if people < M:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid
print(answer)
