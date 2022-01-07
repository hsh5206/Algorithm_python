# 1. 큰 수의 법칙
'''
'큰수의 법칙'은 일반적으로 통계 분야에서 다루어지는 내용이지만 동빈이는 본인만의 방식으로 다르게 사용하고 있다.
동빈이의 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.

ex)
N = 5, M = 8, K = 3
2, 4, 5, 4, 6
-> 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5

배열의 크기는 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 동빈이의 큰 수의 법칙에 따른 결과를 출력하시오.

입력:
5 8 3        -> N(2 ~ 1,000), M(1 ~ 10,000), K(1 ~ 10,000)
2 4 5 4 6    -> N개의 자연수 각 (1 ~ 10,000)

출력:
46           -> 큰수의 법칙에 따른 결과
'''

N, M, K = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)

result = 0
while(M > 0):
    for i in range(K):
        result += data[0]
        M -= 1
        if(M == 0):
            break
    if(M != 0):
        result += data[1]
        M -= 1

print(result)

# 다른 풀이
'''
count = int(M / (K + 1)) * K
count += M % (K + 1)

result = 0
result += (count) * data[0]
result += (M - count) * data[1]

print(result)
'''
