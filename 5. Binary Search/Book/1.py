# 부품찾기

def find(this, start, end):
    while start <= end:
        mid = (start + end) // 2
        if this == component[mid]:
            return True
        elif this < component[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False


N = int(input())
component = list(map(int, input().split()))

M = int(input())
find_list = list(map(int, input().split()))

component.sort()
for i in range(M):
    temp = find(find_list[i], 0, N-1)
    if temp == True:
        print("yes")
    else:
        print("No")
