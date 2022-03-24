# https://programmers.co.kr/learn/courses/30/lessons/12934

from math import sqrt


def solution(n):
    x = sqrt(n)
    return (x+1)**2 if x == int(x) else -1
