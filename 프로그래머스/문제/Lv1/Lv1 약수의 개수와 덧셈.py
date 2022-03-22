import math


def solution(left, right):
    answer = 0
    for x in range(left, right+1):
        if math.sqrt(x) == int(math.sqrt(x)):
            answer -= x
        else:
            answer += x
    return answer
