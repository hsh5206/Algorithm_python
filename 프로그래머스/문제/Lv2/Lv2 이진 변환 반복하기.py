# https://programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    answer = [0, 0]
    while s != '1':
        len_s = len(s)
        s = ''.join(s.split('0'))
        len_ns = len(s)
        s = bin(len(s))[2:]
        answer[0] += 1
        answer[1] += len_s - len_ns
    return answer
