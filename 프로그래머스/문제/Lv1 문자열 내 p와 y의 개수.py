# https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    s = s.lower()
    answer = (s.count('p') == s.count('y'))
    return answer
