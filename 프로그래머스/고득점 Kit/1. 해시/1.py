# 완주하지 못한 선수
def solution(participant, completion):
    info = {}
    for i in participant:
        if info.get(i):
            info[i] += 1
        else:
            info[i] = 1

    for i in completion:
        info[i] -= 1

    answer = ''
    for i, num in info.items():
        if num != 0:
            answer = i
            break
    return answer
