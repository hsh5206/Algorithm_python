# https://programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    s = list(s)
    s.sort(reverse=True)
    return ''.join(s)

def solution2(s):
    return ''.join(sorted(list(s))[::-1])