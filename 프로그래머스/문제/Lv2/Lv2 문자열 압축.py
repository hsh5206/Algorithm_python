# https://programmers.co.kr/learn/courses/30/lessons/60057
# 카카오

import sys


def solution(s):
    if len(s) == 1:
        return 1
    answer = sys.maxsize
    for i in range(1, len(s)//2+1):
        arr = s[:i]
        res = press(s, i, arr)
        answer = min(answer, len(res))
    return answer


def press(s, div, arr):
    count = 1
    res = ''
    for j in range(div, len(s)+1, div):
        if s[j:j+div] == arr:
            count += 1
        else:
            res = res+str(count)+arr if count != 1 else res+arr
            arr = s[j:j+div]
            count = 1
    res = res+str(count)+arr if count != 1 else res+arr
    return res
