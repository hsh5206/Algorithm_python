# 퇴사

N = int(input())
arr = []
for _ in range(N):
    day, pay = map(int, input().split())
    arr.append((day, pay))
dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    day = arr[i][0]
    pay = arr[i][1]
    if day + i <= N:
        dp[i] = max(pay + dp[day+i], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])
