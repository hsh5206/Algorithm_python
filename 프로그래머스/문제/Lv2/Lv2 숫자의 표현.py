# https://programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    i, j = 1, 2
    sum = 1
    result = 0
    while i != j:
        if sum < n:
            sum += j
            j += 1
        else:
            if sum == n:
                result += 1
            sum -= i
            i += 1
    return result
