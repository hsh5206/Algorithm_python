# 그룹 단어 체커

alpha = list('abcdefghijklmnopqrstuvwxyz')

result = 0
N = int(input())
for _ in range(N):
    alpha_num = [0] * 26
    arr = input()
    flag = 0
    for i in range(len(arr)):
        temp = alpha.index(arr[i])
        if alpha_num[temp] == 0:
            alpha_num[temp] += 1
        else:
            if arr[i - 1] == arr[i]:
                alpha_num[temp] += 1
            else:
                flag = 1
    if flag == 0:
        result += 1

print(result)
