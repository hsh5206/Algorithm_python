# 체육복
def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    answer = 0
    for x in (lost-reserve):
        if x-1 in (reserve-lost):
            reserve.remove(x-1)
            continue
        elif x+1 in (reserve-lost):
            reserve.remove(x+1)
            continue
        answer += 1
    return n - answer
