# 프린터
from collections import deque


def solution(priorities, location):
    pri = deque((priorities[i], i) for i in range(len(priorities)))

    answer = 0
    while pri:
        now, index = pri.popleft()

        isAppend = False
        for nnow, nindex in pri:
            if now < nnow:
                isAppend = True
                break

        if isAppend:
            pri.append((now, index))
        else:
            answer += 1
            if index == location:
                return answer
