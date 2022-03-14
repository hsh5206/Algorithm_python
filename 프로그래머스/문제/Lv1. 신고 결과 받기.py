from collections import defaultdict


def solution(id_list, reports, k):
    reported = dict()
    for report in reports:
        x, y = report.split(' ')
        if not reported.get(y):
            reported[y] = set([x])
        else:
            reported[y].add(x)

    result = defaultdict(int)
    for id in id_list:
        if reported.get(id) and len(reported[id]) >= k:
            for x in reported[id]:
                result[x] += 1

    answer = [0] * len(id_list)
    for i, id in enumerate(id_list):
        answer[i] = result[id]
    return answer
