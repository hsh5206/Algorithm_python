# 카펫
def solution(brown, yellow):
    answer = []
    for i in range(2, brown, 2):
        row = (brown - i) // 2
        column = i // 2 + 2
        if row < column:
            break
        temp = (row-2) * (column-2)
        if temp > 0 and temp == yellow:
            answer = [row, column]
    return answer
