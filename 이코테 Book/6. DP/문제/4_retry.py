# 효율적인 화폐 구성

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 dp 테이블
dp = [-1] * (M + 1)

# DP
dp[0] = 0
for i in range(N):
    for j in range(arr[i], M+1):
        if dp[j - arr[i]] != -1:  # i-k원을 만드는 방법이 존재하는 경우
            dp[j] = min(dp[j], dp[j - arr[i]] + 1)

# 계산된 결과 출력
print(dp[M])
