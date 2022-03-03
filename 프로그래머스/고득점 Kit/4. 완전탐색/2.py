# 소수 찾기
import math
from itertools import permutations as perm


def solution(numbers):
    arr = set()
    for x in range(1, len(numbers)+1):
        temp = set(perm(numbers, x))
        for x in temp:
            str = ''.join(x)
            number = int(str)
            arr.add(number)

    answer = 0
    for x in arr:
        if check(x):
            answer += 1
    return answer


def check(number):
    if number == 0 or number == 1:
        return False
    for x in range(2, int(math.sqrt(number))+1):
        if number % x == 0:
            return False
    return True
