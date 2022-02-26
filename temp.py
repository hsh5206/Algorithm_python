A, B, V = map(int, input().split())
result = (V-B)/(A-B)
print(int(result) if result == int(result) else int(result)+1)
