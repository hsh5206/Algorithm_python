# 카누 선수

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k, n = map(int, input().split())
    arr = []
    for _ in range(4):
        arr.append(list(map(int, input().split())))

    one, two = set(), set()
    for idx in range(0, 4, 2):
        for x in arr[idx]:
            for y in arr[idx+1]:
                one.add(x+y) if idx == 0 else two.add(x+y)
    one = sorted(list(one))
    two = sorted(list(two))

    # 투포인터
    result = 0
    diff = sys.maxsize
    left, right = 0, len(two)-1
    while left < len(one) and 0 <= right:
        temp = one[left]+two[right]-k
        if abs(temp) < diff:
            diff = abs(temp)
            result = temp + k
        elif abs(temp) == diff:
            result = min(result, temp+k)
        if temp < 0:
            left += 1
        elif temp > 0:
            right -= 1
        else:
            break

    print(result)
