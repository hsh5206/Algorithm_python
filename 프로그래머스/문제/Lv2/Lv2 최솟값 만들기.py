# https://programmers.co.kr/learn/courses/30/lessons/12941

def solution(A, B):
    N = len(A)
    A.sort()
    B.sort(reverse=True)
    result = 0
    for i in range(N):
        result += A[i]*B[i]
    return result
