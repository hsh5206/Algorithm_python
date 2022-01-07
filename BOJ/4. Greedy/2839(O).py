# 설탕 배달

n = int(input())
a = 5
b = 3
count = 0

if(n >= 5):
    count += n // 5
    n = n % 5
if(n % 3 == 0):
    count += n // 3
else:
    temp = count
    for i in range(0, count+1):
        if(temp > 0):
            n += 5
            temp -= 1
            if(n % 3 == 0):
                temp += n // 3
                count = temp
                break
            elif(i == count):
                count = -1
                break
            else:
                continue
        else:
            count = -1

print(count)
