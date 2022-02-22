T = int(input())

for _ in range(T):
    floor, where = int(input()), int(input())
    num = [[i for i in range(where+1)] for _ in range(floor+1)]
    for p in range(1, len(num)):
        for i in range(len(num[p])):
            num[p][i] = sum(num[p-1][:i+1])
    print(num[floor][where])
