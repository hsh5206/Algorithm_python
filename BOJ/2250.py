# 트리의 높이와 너비
from collections import defaultdict


class Node:
    def __init__(self, parent, node, left, right):
        self.parent = parent
        self.node = node
        self.left = left
        self.right = right


def get(level):
    global position
    if node.left_node != -1:
        get(tree[node.left_node], level + 1)  # 왼쪽 노드가 있는 경우 먼저 방문, 레벨 + 1

    position += 1  # 해당 노드의 위치 지정
    if level in result:
        # 해당 레벨에 이미 다른 노드의 위치가 들어가 있는 경우 리스트 뒤에 추가
        result[level].append(position)
    else:
        result[level] = [position]  # 해당 레벨에 노드가 처음인 경우 리스트 형태로 노드 위치 추가

    if node.right_node != -1:
        get(tree[node.right_node], level + 1)


N = int(input())
node, left, right = map(int, input().split())
tree = dict()

for i in range(1, N + 1):
    tree[i] = Node(i, -1, -1, -1)

for _ in range(N):
    p, left, right = map(int, input().split())
    if left != -1:
        tree[p].left_node = left
        tree[left].parent = p
    if right != -1:
        tree[p].right_node = right
        tree[right].parent = p

result = defaultdict(list)
answer = [0, 0]
for x in sorted(result.keys()):
    result[x].sort()
if result[x][-1]-result[x][0]+1 > answer[1]:
    answer[0] = x
    answer[1] = result[x][-1]-result[x][0]+1
print(*answer)
