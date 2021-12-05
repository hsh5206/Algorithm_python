# ATM
n = int(input())
times = list(map(int, input().split()))

times.sort()

result = 0
n = len(times)
for i in range(len(times)):
    result += times[i]*n
    n -= 1

print(result)
