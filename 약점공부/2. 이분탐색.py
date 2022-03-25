# 이분탐색
arr = [1, 2, 4, 5, 8, 9]

target = 4

while start <= end:
    mid = (start + end) // 2
    if arr[mid] > target:
        end = mid - 1
    elif arr[mid] < target:
        start = mid + 1
    else:
        print(mid)
        break
