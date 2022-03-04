# 가장 큰 수
# def solution(numbers):
#     max_len = len(str(max(numbers)))
#     numbers = [[str(i), str(i)] for i in numbers]
#     for i in range(len(numbers)):
#         temp = numbers[i][0]
#         numbers[i][0] += temp * (max_len//len(temp))
#         numbers[i][0] += temp[-1] * (max_len % len(temp))
#     numbers.sort(reverse=True)
#     answer = int(''.join([x[1] for x in numbers]))
#     return str(answer)

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3)
    numbers.reverse()
    answer = int(''.join(numbers))
    return str(answer)
