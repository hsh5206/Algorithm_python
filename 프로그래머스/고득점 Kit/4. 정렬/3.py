# H-index
# def solution(citations):
#     quote = [0] * 10001
#     citations.sort(reverse=True)

#     n = 0
#     for x in citations:
#         n += 1
#         quote[x] = n

#     for x in citations:
#         for i in range(x-1, -1, -1):
#             if quote[i] == 0:
#                 quote[i] = quote[x]
#             else:
#                 break

#     answer = 0
#     for i, x in enumerate(quote):
#         if x != 0:
#             if x >= i:
#                 answer = i
#         else:
#             break
#     return answer

def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    for x in citations:
        if x > answer:
            answer += 1
        else:
            break
    return answer
