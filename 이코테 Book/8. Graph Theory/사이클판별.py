# 사이클 판별 알고리즘 with 서로소 집합
# 무방향 그래프에서의 사이클 판별 (방향은 DFS)
# 1. 각 간선을 하나씩 확인하며 두 노드의 루트 노드를 확인
# - 루트 노드가 다르면 합집합 연산 수행
# - 루트 노드가 같다면 사이클 발생
# 2. 그래프의 모든 간선에 1번과정 반복

# 특정 원소가 속한 집합을 찾기 - 경로 압축
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

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

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합 연산 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클 발생")
else:
    print("사이클 없음")
