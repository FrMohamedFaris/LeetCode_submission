# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def createBinaryTree(self, descriptions):

        node = {}
        parents = set()
        children = set()

        for p, c, isleft in descriptions:
            if p not in node:
                node[p] = TreeNode(p)
            if c not in node:
                node[c] = TreeNode(c)

            if isleft:
                node[p].left = node[c]
            else:
                node[p].right = node[c]

            parents.add(p)
            children.add(c)

        root_val = (parents - children).pop()
        return node[root_val]


def printPreOrder(node):
    if node:
        print(node.val),
        printPreOrder(node.left)
        printPreOrder(node.right)


descriptions = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]
sol = Solution()
root = sol.createBinaryTree(descriptions)
printPreOrder(root)
