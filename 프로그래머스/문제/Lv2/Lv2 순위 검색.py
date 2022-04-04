# https://programmers.co.kr/learn/courses/30/lessons/72412

from collections import defaultdict
from itertools import combinations as comb


def solution(info, query):
    global answer
    answer = []
    dict = defaultdict(list)
    for inf in info:
        i = inf.split()
        add(i[:-1], dict, int(i[-1]))
    for key in dict.keys():
        dict[key].sort()
    for q in query:
        temp = q.replace('and', '').replace('-', '').split()
        key = ''.join(temp[:-1])
        find(key, dict, int(temp[-1]))
    return answer


def add(key, dict, score):
    for k in range(5):
        change = list(comb(key, k))
        for l in change:
            dict[''.join(l)].append(score)


def find(key, dict, score):
    global answer
    arr = dict[key]
    left, right = 0, len(arr)
    while left < right:
        mid = (left+right)//2
        if arr[mid] >= score:
            right = mid
        else:
            left = mid + 1
    answer.append(len(arr)-left)
