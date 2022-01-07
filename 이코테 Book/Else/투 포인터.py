# 투 포인터 알고리즘
# 리스트에 순차적을 접근 해야 할 때 두개의 점의 위치를 기록하면서 처리
# 시적점과 끝점으로 접근할 데이터의 범위 표현
# ex) 특정한 합을 가지는 부분 연속 수열 찾기 (합이 M인 부분 연속 수열의 개수)
# 방법
# 1. 시작점과 끝점이 첫번째 인덱스를 가리킴
# 2. 현재 부분 합이 M과 같다면, 카운트
# 3. 현재 부분 합이 M보다 작다면, end를 1 증가
# 4. 현재 부분 합이 M보다 크거나 같다면, start를 1 증가
# 5. 2~4 반복

n = 5  # 데이터의 개수
m = 5  # 찾고자 하는 부분합
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키면서 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
        # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]
