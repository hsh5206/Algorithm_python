# 연산자 끼워 넣기
# 중복순열로 풀어보기 product

import itertools

N = input()
arr = []
arr = list(map(int, input().split()))
do = []
do = list(map(int, input().split()))

temp = []
for i in range(len(do)):
    while do[i] > 0:
        temp.append(i)
        do[i] -= 1

fin = []
result = arr[0]
for k in itertools.permutations(temp):
    j = 0
    for i in range(1, len(arr)):
        if k[j] == 0:  # +
            result += arr[i]
        elif k[j] == 1:  # -
            result -= arr[i]
        elif k[j] == 2:  # *
            result *= arr[i]
        else:  # //
            flag = 0
            if result < 0:
                result = -result
                flag = 1
            result = result // arr[i]
            if flag == 1:
                result = -result
        j += 1
    fin.append(result)
    result = arr[0]

print(max(fin), min(fin))
