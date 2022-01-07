# 30
N = input()
arr = [0 for _ in range(len(N))]
for i in range(len(N)):
    arr[i] = int(N[i])
arr.sort(reverse=True)
result = ''

if arr[-1] == 0:
    sum = 0
    for i in arr:
        sum += i
    if(sum % 3 == 0):
        for i in arr:
            result += str(i)
    else:
        result = -1
else:
    result = -1

print(result)
