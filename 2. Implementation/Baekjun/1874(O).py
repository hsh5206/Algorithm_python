# 스택 수열

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.reverse()

temp = []
result = []
vs = arr.pop()
for n in range(1, N+1):
    temp.append(n)
    result.append("+")
    for i in range(len(temp)-1, -1, -1):
        if temp[i] == vs:
            result.append("-")
            if arr:
                vs = arr.pop()
            temp.pop()
        else:
            break

if temp:
    print("NO")
else:
    for x in result:
        print(x)
