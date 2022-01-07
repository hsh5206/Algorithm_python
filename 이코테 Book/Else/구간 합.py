# 구간 합 문제
# 연속적으로 나열된 N개의 수가 있을 때
# 특정 구간의 모든 수를 합한 값을 계산하는 문제

# 구간 합 빠르게 계산
# 입력 : N(수열의 길이), M(쿼리 정보), (M개의) left right
# 출력 : [left, right] 구간의 데이터들의 합을 출력
# 아이디어 : 접두사 합
# 배열의 맨 앞부터 특정 위치까지의 합을 미리 구해 놓은 것
# ex) 1 2 3  4  5  6  7  8  9 10
# ex) 1 3 6 10 15 21 28 36 45 55
# 3 ~ 9의 합 = 45 - 3 = 42
# [i, j]의 합 = p[j] - p[i -1]

# 데이터의 개수 N과 데이터 입력받기
n = 5
data = [10, 20, 30, 40, 50]
# 접두사 합 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# 구간 합 계산(세 번째 수부터 네 번째 수까지)
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])
