# n진수 게임
alpha = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def solution(n, t, m, p):
    all = ''
    temp = 0
    needs = p
    for _ in range(t-1):
        needs += m
    while True:
        if len(all) > needs:
            break
        all_temp = ''
        temp2 = temp
        while True:
            k = temp2 % n
            if k in alpha:
                k = alpha[k]
            all_temp = str(k) + all_temp
            if temp2 // n != 0:
                temp2 = temp2 // n
            else:
                break
        all += all_temp
        temp += 1

    answer = ''
    for i in range(p-1, (t-1)*m+p, m):
        answer += str(all[i])

    return answer


print(solution(16, 16, 2, 1))
