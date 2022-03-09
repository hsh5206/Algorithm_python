# 크게 만들기
N, K = map(int, input().split())
arr = list(map(int, input().strip()))

result = []
for x in arr:
    if not result:
        result.append(x)
        continue
    while result and result[-1] < x and K != 0:
        K -= 1
        result.pop()
    result.append(x)

while K != 0:
    K -= 1
    result.pop()

print(*result, sep='')
