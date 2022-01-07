# 계수정렬
# 데이터 개수 N 데이터의 최댓값 K
# 최악 : O(N+K)

# 모든 원소의 값이 0보다 크거나 같다고 가정
arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로)
count = [0]*(max(arr) + 1)

for i in range(len(arr)):
    count[arr[i]] += 1  # 각 데이터에 해당하는 인덱스 값 증가

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
