from idlelib.tree import TreeNode


class Solution:
    def __init__(self):
        self.totalSum = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root is None:
            return

        self.bstToGst(root.right)
        self.totalSum = self.totalSum + root.val
        root.val = self.totalSum
        self.bstToGst(root.left)
        return root


arr = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
sol = Solution(arr)
print(sol)
