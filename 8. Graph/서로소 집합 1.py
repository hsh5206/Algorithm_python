# 서로소 집합 자료구조
# 합집합 -> 두 개의 원소가 포함된 집합을 하나로
# 찾기 -> 특정 원소가 속한 집합이 어떤 집합인지
# 과정
# 1. 합집합 연산을 확인 하여, 서로 연결된 두 노드 A,B를 확인
# - A와 B의 루트 노드 A',B'을 각각 찾기
# - A'을 B'의 부모 노드 설정
# 2. 모든 합집합 연산을 처리할 때까지 1번의 과정 반복

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, int().split())
# 부모 테이블 초기화
parent = [0] * (v + 1)

# 부모 테이블상에 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소각 속한 집합 출력하기
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')
