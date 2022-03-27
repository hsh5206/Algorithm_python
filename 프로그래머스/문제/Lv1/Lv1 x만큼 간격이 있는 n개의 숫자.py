# https://programmers.co.kr/learn/courses/30/lessons/12954
def solution(x, n):
    answer = [x for _ in range(n)]
    if x != 0:
        answer = [i for i in range(
            x, x*n+1, x)] if x > 0 else [i for i in range(x, x*n-1, x)]
    return answer
