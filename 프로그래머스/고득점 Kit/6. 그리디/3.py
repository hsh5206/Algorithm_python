# 큰 수 만들기
def solution(number, k):
    answer = []
    for x in number:
        if k == 0:
            answer.append(x)
        elif not answer:
            answer.append(x)
        else:
            while answer and int(answer[-1]) < int(x) and k > 0:
                answer.pop()
                k -= 1
            answer.append(x)
    answer = answer[:len(answer)-k]
    return ''.join(answer)
