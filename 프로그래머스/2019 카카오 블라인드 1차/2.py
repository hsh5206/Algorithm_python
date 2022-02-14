def solution(N, stages):
    answer = [[i, 0] for i in range(N+2)]
    arrive = [0] * (N+2)
    for x in stages:
        arrive[x-1] += 1
    for i in range(len(arrive)-1, 0, -1):
        arrive[i-1] += arrive[i]
    for i in range(1, len(arrive)):
        if arrive[i-1] != 0:
            answer[i][1] = (arrive[i-1] - arrive[i]) / arrive[i-1]
    answer.sort(key=lambda x: -x[1])
    result = []
    for i, x in answer:
        if i != 0 and i != len(answer)-1:
            result.append(i)
    return result


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
