def solution(sizes):
    x, y = 0, 0
    for t in sizes:
        t.sort()
        x = max(x, t[0])
        y = max(y, t[1])
    return x*y
