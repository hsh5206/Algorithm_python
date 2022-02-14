import sys
sys.setrecursionlimit = 10**4


class Node:
    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y
        self.left = None
        self.right = None


class Tree:
    def __init__(self, index, x, y):
        self.head = Node(index, x, y)

    def insert(self, index, x, y):
        curr = self.head
        while True:
            if curr.x > x:
                if curr.left == None:
                    curr.left = Node(index, x, y)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right == None:
                    curr.right = Node(index, x, y)
                    break
                else:
                    curr = curr.right

    def pre(self):
        result = []

        def do(curr):
            result.append(curr.index)
            if curr.left != None:
                do(curr.left)
            if curr.right != None:
                do(curr.right)
        do(self.head)
        return result

    def post(self):
        result = []

        def do(curr):
            if curr.left != None:
                do(curr.left)
            if curr.right != None:
                do(curr.right)
            result.append(curr.index)
        do(self.head)
        return result


def solution(nodeinfo):
    nodes = [[i+1, nodeinfo[i]] for i in range(len(nodeinfo))]
    nodes.sort(key=lambda x: [-x[1][1], x[1][0]])
    tree = Tree(nodes[0][0], nodes[0][1][0], nodes[0][1][1])
    for node in nodes[1:]:
        tree.insert(node[0], node[1][0], node[1][1])

    pre = tree.pre()
    post = tree.post()

    answer = [pre, post]
    return answer


print(solution([[5, 3], [11, 5], [13, 3], [3, 5],
      [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
