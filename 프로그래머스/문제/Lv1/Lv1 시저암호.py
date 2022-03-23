# https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''
    for x in s:
        if x == ' ':
            answer += ' '
            continue
        temp = ord(x)+n
        if x.isupper():
            temp = temp if temp <= ord('Z') else ord('A')+temp-ord('Z')-1
        elif x.islower():
            temp = temp if temp <= ord('z') else ord('a')+temp-ord('z')-1
        answer += chr(temp)
    return answer


def solution2(s, n):
    answer = ''
    for x in s:
        if x == ' ':
            answer += ' '
        else:
            if x.isupper():
                answer += chr((ord(x)-ord('A') + n) % 26+ord('A'))
            elif x.islower():
                answer += chr((ord(x)-ord('a') + n) % 26+ord('a'))
    return answer
