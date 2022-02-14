from itertools import combinations


def solution(relation):
    answer = 0
    N, M = len(relation), len(relation[0])
    arr = []
    for i in range(1, M+1):
        arr.extend(combinations(range(M), i))

    total = []
    for x in arr:
        isOK = True
        for t in total:
            for k in t:
                if k in ''.join(map(str, x)):
                    isOK = False
                else:
                    isOK = True
                    break
            if not isOK:
                break
        if isOK:
            if check(x, relation):
                total.append(list(map(str, x)))
                answer += 1
    return answer


def check(arr, relation):
    isOK = True
    temp = []
    for j in range(len(relation)):
        str = ''
        for i in arr:
            str += relation[j][i]
        if str not in temp:
            temp.append(str)
        else:
            isOK = False
            break
    if isOK:
        return True
    return False


print(solution([["a", "1", "aaa", "c", "ng"],
                ["a", "1", "bbb", "e", "g"],
                ["c", "1", "aaa", "d", "ng"],
                ["d", "2", "bbb", "d", "ng"]]))
