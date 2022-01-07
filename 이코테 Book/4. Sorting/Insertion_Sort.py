# 삽입 정렬
# 최악 : O(N^2) 거의 정렬되어 있으면 매우 빠름
# 최선 : O(N)

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break

print(arr)
