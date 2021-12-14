# 문자열 뒤집기
# X

S = list(map(int, input()))

result1 = 0
result2 = 0
i = 0
for j in range(i + 1, len(S)):
    if S[i] == S[j]:
        continue
    else:
        if S[i] == 0:
            result1 += 1
        else:
            result2 += 1
        i = j

if S[-1] == 0:
    result1 += 1
else:
    result2 += 1

print(min(result1, result2))
