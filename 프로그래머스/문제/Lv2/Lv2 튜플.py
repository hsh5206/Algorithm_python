# https://programmers.co.kr/learn/courses/30/lessons/64065

import re


def solution(s):
    result = re.findall('[{][\d,]+[}]', s)
    result.sort(key=lambda x: len(x))
    answer = []
    now = set()
    for x in result:
        next = set(list(x[1:-1].split(',')))
        num = list(next - now)[-1]
        answer.append(int(num))
        now = next
    return answer
