# 압축
alpha = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
         'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}


def solution(msg):
    answer = []
    left, right = 0, 1
    start = 0
    while right <= len(msg):
        temp = msg[left:right]
        if temp in alpha:
            if start != 0:
                answer.pop()
            answer.append(alpha[temp])
            right += 1
            start += 1
        else:
            alpha[temp] = len(alpha)+1
            left += 1
            start = 0

    return answer


print(solution('KAKAO'))
