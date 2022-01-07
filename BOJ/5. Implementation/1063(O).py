# 킹

king, rock, N = map(list, input().split())
temp = ''
for i in range(len(N)):
    temp += N[i]
n = int(temp)

king[0] = ord(king[0]) - 64 - 1
king[1] = 8 - int(king[1])
rock[0] = ord(rock[0]) - 64 - 1
rock[1] = 8 - int(rock[1])

loc_k = [king[1], king[0]]
loc_r = [rock[1], rock[0]]

dx = [0, 0, 1, -1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
dirc = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']

direction = []
for _ in range(n):
    direction.append(input())

x, y = loc_k
a, b = loc_r
for t in direction:
    k = dirc.index(t)
    nx = x + dx[k]
    ny = y + dy[k]
    na = a + dx[k]
    nb = b + dy[k]
    if 0 <= na < 8 and 0 <= nb < 8 and nx == a and ny == b:
        a = na
        b = nb
    if 0 <= nx < 8 and 0 <= ny < 8 and (nx != a or ny != b):
        x = nx
        y = ny

print(chr(y+65)+str(8-x))
print(chr(b+65)+str(8-a))
