# 가장 긴 증가하는 부분 수열(LIS) 알고리즘
# D[i] = arr[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
# 점화식: D[i] = max(D[i], D[j] + 1)
# if arr[j] < arr[i]
# (0 <= i < j)

N = int(input())
arr = list(map(int, input().split()))
# arr.reverse() # 리스트 뒤집기 -> 가장 긴 감소하는 부분 수열

dp = [1] * N

# LIS 알고리즘
for i in range(1, N):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
