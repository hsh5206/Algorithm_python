import math
from itertools import combinations as comb


def solution(nums):
    sum_list = [sum(i) for i in list(comb(nums, 3))]
    answer = 0
    for x in sum_list:
        isOK = True
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                isOK = False
                break
        if isOK:
            answer += 1
    return answer
