# https://programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations as perm


def solution(k, dungeons):
    answer = 0
    for order in list(perm(dungeons, len(dungeons))):
        answer = max(answer, enter_dungeons(order, k))
        if answer == len(dungeons):
            break
    return answer


def enter_dungeons(arr, now):
    enter = 0
    for require, use in arr:
        if require <= now:
            now -= use
            enter += 1
    return enter
