# 트리의 높이와 너비
from collections import defaultdict


class Node:
    def __init__(self, index, depth):
        self.index = index
        self.left = None
        self.right = None
        self.depth = depth


class Tree:
    def __init__(self, index, depth):
        self.max_depth = 0
        self.head = Node(index, depth)
        self.head.left = None
        self.head.right = None

    def add(self, index, left, right):
        current, depth = self.find(self.head, index)
        if left != -1:
            current.left = Node(left, depth)
            self.max_depth = max(self.max_depth, depth)
        if right != -1:
            current.right = Node(right, depth)
            self.max_depth = max(self.max_depth, depth)

    def find(self, node, index):
        current = node
        if current.index == index:
            return [current, current.depth+1]
        if current.left != None:
            temp = self.find(current.left, index)
            if temp:
                return temp
        if current.right != None:
            temp2 = self.find(current.right, index)
            if temp2:
                return temp2

    def get(self, result):
        global num
        num = 1

        def do(curr):
            global num
            if curr.left != None:
                do(curr.left)
            result[curr.depth].append(num)
            num += 1
            if curr.right != None:
                do(curr.right)

        do(self.head)


N = int(input())
T = Tree(1, 1)
for _ in range(N):
    node, left, right = map(int, input().split())
    T.add(node, left, right)
result = defaultdict(list)
T.get(result)
answer = [0, 0]
for x in range(1, T.max_depth+1):
    result[x].sort()
    if answer[1] < (result[x][-1]-result[x][0]+1):
        answer = [x, result[x][-1]-result[x][0]+1]
print(*answer)
