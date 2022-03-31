# https://programmers.co.kr/learn/courses/30/lessons/72411
from collections import defaultdict
from itertools import combinations as comb


def solution(orders, course):
    # 모든 조합을 딕셔너리에 기록
    dict = defaultdict(int)
    for x in orders:
        get_all_comb(list(x), course, dict)
    # 횟수가 2이상인 조합만 [조합, 횟수]으로 result에 append
    result = [[i, dict[i]] for i in dict if dict[i] >= 2]
    # 횟수가 큰 순서로 정렬
    result.sort(key=lambda x: -x[1])
    answer = []
    added = {}  # 해당 매뉴의 횟수 기록
    # 메뉴 확정
    for x in result:
        # 해당 메뉴가 없으면 추가
        if len(x[0]) not in added:
            answer.append(x[0])
            added[len(x[0])] = x[1]
        # 해당 메뉴가 있지만 횟수가 같으면 추가
        elif added[len(x[0])] == x[1]:
            answer.append(x[0])
    return sorted(answer)


def get_all_comb(arr, course, dict):
    for i in course:
        for x in list(comb(arr, i)):
            dict[''.join(sorted(list(x)))] += 1
