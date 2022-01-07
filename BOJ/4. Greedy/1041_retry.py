# 주사위

N = int(input())
dice = list(map(int, input().split()))
result = 0

if N == 1:
    print(sum(dice) - max(dice))
else:
    sum = [min(dice[0], dice[5]), min(
        dice[1], dice[4]), min(dice[2], dice[3])]
    sum.sort()

    n1 = (N-2)*(N-2) + (N-1)*(N-2)*4
    n2 = (N-2)*4 + (N-1)*4
    n3 = 4

    result = n1*sum[0] + n2*sum[:2] + n3*sum(sum)

print(result)
