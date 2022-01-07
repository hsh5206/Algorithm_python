# 문자열 재정렬
# O

S = input()

result = []
num = 0
for data in S:
    if data.isalpha():
        result.append(data)
    else:
        num += int(data)

result.sort()
for res in result:
    print(res, end='')
print(num)
