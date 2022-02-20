# 위장
def solution(clothes):
    answer = 1
    items = dict()
    for _, where in clothes:
        if items.get(where):
            items[where] += 1
        else:
            items[where] = 1
    for _, num in items.items():
        answer *= (num+1)
    answer -= 1
    return answer
