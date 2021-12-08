# 퀵 정렬
# 평균 : O(NlogN)
# 최악 : O(N^2)

arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(arr, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return
    pivot = start  # 피봇은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피봇보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and arr[left] <= arr[pivot]):
            left += 1
        # 피봇보다 작은 데이터를 찾을 때까지 반복
        while(right > start and arr[right] >= arr[pivot]):
            right -= 1
        if(left > right):  # 엇갈렸다면 작은 데이터와 피봇을 교체
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            arr[left], arr[right] = arr[right], arr[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


def quick_sort_2(arr):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  # 피봇은 첫 번째 원소
    tail = arr[1:]  # 피봇을 제외한 리스트 (리스트 슬라이싱)

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분 (리스트 컴프리헨션)
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분 (리스트 컴프리헨션)

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트 반환
    return quick_sort_2(left_side) + [pivot] + quick_sort_2(right_side)


quick_sort(arr, 0, len(arr) - 1)
print(arr)
