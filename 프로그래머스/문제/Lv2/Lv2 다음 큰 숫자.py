# https://programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    cnt = bin(n)[2:].count('1')
    result = 0
    for x in range(n+1, 1000001):
        if bin(x)[2:].count('1') == cnt:
            result = x
            break
    return result


print(solution(78))
