# 모의고사
def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    thr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    one = one*(len(answers)//len(one)) + one[:(len(answers) % len(one))]
    two = two*(len(answers)//len(two)) + two[:(len(answers) % len(two))]
    thr = thr*(len(answers)//len(thr)) + thr[:(len(answers) % len(thr))]

    result = [0, 0, 0]
    for i in range(len(answers)):
        if one[i] == answers[i]:
            result[0] += 1
        if two[i] == answers[i]:
            result[1] += 1
        if thr[i] == answers[i]:
            result[2] += 1

    answer = [i+1 for i in range(len(result)) if result[i] == max(result)]
    return answer
