from itertools import combinations as comb


def solution(numbers):
    arr = list(comb(numbers, 2))
    answer = [sum(temp) for temp in arr]
    answer = sorted(list(set(answer)))
    return answer
