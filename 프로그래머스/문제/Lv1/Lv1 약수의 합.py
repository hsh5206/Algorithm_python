# https://programmers.co.kr/learn/courses/30/lessons/12928
from math import sqrt


def solution(n):
    if n == 0 or n == 1:
        return n
    answer = n+1
    for x in range(2, int(sqrt(n))+1):
        if n % x == 0:
            answer += sum(set([x, n//x]))
    return answer
