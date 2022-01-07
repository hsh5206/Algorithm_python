# 셀프 넘버

N = 10000
self_num = [0 for _ in range(N)]
result = [0 for _ in range(N)]


def find_self_num(num):
    temp = 0
    temp_num = num
    temp = temp_num + temp_num // 1000
    temp_num = temp_num % 1000
    temp += temp_num // 100
    temp_num = temp_num % 100
    temp += temp_num // 10
    temp_num = temp_num % 10
    temp += temp_num
    return temp


for i in range(N):
    self_num[i] = i+1
    result[i] = i+1

self_num.sort(reverse=True)

for num in self_num:
    temp = find_self_num(num)
    if temp in result:
        result.remove(temp)
    else:
        continue

for num in result:
    print(num)
