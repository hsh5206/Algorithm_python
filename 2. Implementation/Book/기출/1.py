# 럭키 스트라이크
# O

N = list(map(int, input()))
length = len(N)

sum1 = 0
for i in range(length // 2):
    sum1 += N[i]

sum2 = 0
for i in range(length//2, length):
    sum2 += N[i]

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")
