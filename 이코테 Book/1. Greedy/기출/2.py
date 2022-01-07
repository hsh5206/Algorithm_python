# 곱하기 혹은 더하기
# O

S = list(map(int, input()))

result = S[0]
for i in range(1, len(S)):
    if result == 0 or S[i] == 0:
        result += S[i]
    else:
        result *= S[i]

print(result)
