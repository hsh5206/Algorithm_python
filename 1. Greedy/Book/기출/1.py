# 모험가 길드
# O
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
count = 1
result = 0
now = 0
for i in range(N):
    now = max(now, arr[i])  # 정렬이 되어 있어서 다음은 어차피 큰 수이므로 max와 now 사용 안해도 됨
    if now <= count:
        result += 1
        count = 1
        now = 0
    else:
        count += 1

print(result)
