def solution(lottos, win_nums):
    minimum, maximum = 0, 0
    for x in lottos:
        if x in win_nums:
            minimum += 1
    minimum = 7 - minimum
    maximum = minimum - lottos.count(0)

    answer = [6 if maximum == 7 else maximum, 6 if minimum == 7 else minimum]
    return answer
