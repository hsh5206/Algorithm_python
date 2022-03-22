from collections import defaultdict


def solution(numbers, hand):
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]

    # 숫자의 위치 딕셔너리 정의
    location = defaultdict(list)
    for i in range(4):
        for j in range(3):
            temp = i * 3 + j + 1
            if arr[i][j] == temp:
                location[temp] = [i, j]
            if arr[i][j] == 0:
                location[0] = [i, j]

    #  L로 누룰지 R로 누룰지
    answer = ''
    L, R = [3, 0], [3, 2]
    for x in numbers:
        if x in [1, 4, 7]:
            answer += 'L'
            L = location[x]
        elif x in [3, 6, 9]:
            answer += 'R'
            R = location[x]
        else:
            left_dist = abs(L[0]-location[x][0]) + abs(L[1]-location[x][1])
            right_dist = abs(R[0]-location[x][0]) + abs(R[1]-location[x][1])
            if left_dist < right_dist:
                answer += 'L'
                L = location[x]
            elif left_dist > right_dist:
                answer += 'R'
                R = location[x]
            else:
                if hand == 'left':
                    answer += 'L'
                    L = location[x]
                else:
                    answer += 'R'
                    R = location[x]
    return str(answer)
