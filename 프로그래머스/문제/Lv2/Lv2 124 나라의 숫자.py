# https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    dic = {1: 1, 2: 2, 0: 4}
    result = ''
    while n:
        result += str(dic[n % 3])
        n = n//3 if n % 3 else n//3-1
    return result[::-1]
