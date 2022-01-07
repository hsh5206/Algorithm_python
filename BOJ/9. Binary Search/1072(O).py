# 게임

x, y = map(int, input().split())

z = (y*100) // x

start = 0
end = x

result = 0
flag = 0
while start <= end:
    mid = (start + end) // 2
    a = x + mid
    b = y + mid
    temp = (b*100) // a
    if temp <= z:
        start = mid + 1
    else:
        result = mid
        end = mid - 1
        flag = 1

if flag == 0:
    result = -1

print(result)
