# 한수

N = int(input())

result = 99
for x in range(1, N+1):
    if x <= 99:
        result = x
    else:
        a = x // 100
        b = (x % 100) // 10
        c = (x % 100) % 10
        if (b - a) == (c - b):
            result += 1

print(result)
