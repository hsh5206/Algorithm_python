# 문자열

x, y = input().split()

result = 0
for i in range(abs(len(x)-len(y))+1):
    count = 0
    if len(x) < len(y):
        for j in range(len(x)):
            if x[j] == y[j+i]:
                count += 1
        result = max(result, count)
    else:
        for j in range(len(x)):
            if x[j+i] == y[j]:
                count += 1
        result = max(result, count)

if len(x) < len(y):
    final = len(x) - result
else:
    final = len(y) - result

print(final)
