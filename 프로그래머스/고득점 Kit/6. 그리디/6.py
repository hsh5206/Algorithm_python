# 단속카메라
def solution(routes):
    routes.sort(key=lambda x: x[1])
    now = -30000
    answer = 0
    for start, end in routes:
        if now < start:
            answer += 1
            now = end
    return answer
