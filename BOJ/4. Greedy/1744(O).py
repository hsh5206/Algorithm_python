# 수 묶기

import sys
input = sys.stdin.readline

N = int(input())

pos = []
neg = []
one = []
for _ in range(N):
    x = int(input())
    if x > 1:
        pos.append(x)
    elif x <= 0:
        neg.append(x)
    else:
        one.append(x)
pos.sort(reverse=True)
neg.sort()

result = 0
if len(pos) % 2 == 0:
    for i in range(0, len(pos), 2):
        result += pos[i] * pos[i+1]
else:
    for i in range(0, len(pos)-1, 2):
        result += pos[i] * pos[i+1]
    result += pos[-1]

if len(neg) % 2 == 0:
    for i in range(0, len(neg), 2):
        result += neg[i] * neg[i+1]
else:
    for i in range(0, len(neg)-1, 2):
        result += neg[i] * neg[i+1]
    result += neg[-1]

result += sum(one)
print(result)
