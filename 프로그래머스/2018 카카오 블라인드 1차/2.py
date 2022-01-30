# 다트 게임
def solution(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = ['*', '#']

    dart = []
    dartResult = dartResult.replace('10', 't')

    for i in range(len(dartResult)):
        if dartResult[i] == 't':
            dart.append('10')
        else:
            dart.append(dartResult[i])

    result = []
    number = 0
    for x in dart:
        if x not in bonus and x not in option:
            result.append(number)
            number = 0
            number += int(x)
        elif x in bonus:
            number = number ** bonus[x]
        elif x in option:
            if x == '*':
                number *= 2
                if len(result) >= 1:
                    result[-1] *= 2
            else:
                number *= -1
    result.append(number)

    answer = sum(result)
    return answer
