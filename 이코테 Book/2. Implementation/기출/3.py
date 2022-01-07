# 문자열 압축
S = input()
length = len(S)

result = 0
target = 1
fin = int(1e9)
while True:
    result = length
    if target > length//2:
        break
    temp_result = 1
    temp = S[0:target]
    for i in range(target, length, target):
        if temp == S[i:i + target]:
            if (i+target) == (length):
                temp_result += 1
                result -= (temp_result * target - (1 + target))
                temp_result = 0
                break
            temp_result += 1
        elif temp != S[i:i + target]:
            if temp_result > target:
                result -= (temp_result * target - (1 + target))
                temp_result = 0
            temp = S[i:i + target]
    fin = min(fin, result)
    target += 1

print(fin)
