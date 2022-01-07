# 리모컨

import sys
input = sys.stdin.readline
N = int(input())
M = int(input().strip())
temp = list(input().strip())


def check(num):
    num = list(str(num))
    for i in num:
        if i in temp:
            return False
    return True


result = abs(N - 100)
for i in range(1000001):
    if check(i):
        result = min(result, len(str(i))+abs(i-N))

print(result)
