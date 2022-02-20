N = int(input())

result = 1
i = 2
start = 1
end = start + 6
while True:
    if N == 1:
        break
    if start < N <= end:
        result += 1
        break
    start = end
    end += 6 * i
    i += 1
    result += 1


print(result)
