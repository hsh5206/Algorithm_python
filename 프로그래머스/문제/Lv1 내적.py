def solution(a, b):
    answer = [i*j for i, j in zip(a, b)]
    return sum(answer)
