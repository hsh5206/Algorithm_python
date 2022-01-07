# 괄호

N = int(input())
for _ in range(N):
    arr = list(input())
    flag = 0
    for i in range(len(arr)):
        if arr[i] == '(':
            flag += 1
        else:
            flag -= 1
        if flag < 0:
            print("NO")
            break
    if flag == 0:
        print("YES")
    elif flag > 0:
        print("NO")
