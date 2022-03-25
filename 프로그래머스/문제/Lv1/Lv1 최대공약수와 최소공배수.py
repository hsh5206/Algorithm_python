# https://programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    answer = []
    for i in range(n, 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
    for i in range(m, n*m+1, m):
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break
    return answer


def solution2(n, m):
    a, b = sorted([n, m], reverse=True)
    r = 1
    while r > 0:
        r = a % b
        a, b = b, r
    answer = [a, int(n*m/a)]
    return answer
