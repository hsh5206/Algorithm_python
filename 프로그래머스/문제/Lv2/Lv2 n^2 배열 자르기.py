# https://programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    arr = []
    for i in range(left, right+1):
        arr.append(max(i // n, i % n)+1)
    return arr
