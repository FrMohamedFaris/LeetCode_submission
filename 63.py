class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_level_order(arr, root, i, n):
    if i < n:
        temp = None
        if arr[i] is not None:
            temp = TreeNode(arr[i])
            root = temp
            root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
            root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root


class Solution(object):
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.cumulative_sum = 0
        self.reverse_inorder(root)
        return root

    def reverse_inorder(self, node: TreeNode):
        if node is None:
            return

        self.reverse_inorder(node.right)

        self.cumulative_sum += node.val
        node.val = self.cumulative_sum

        self.reverse_inorder(node.left)


def print_inorder(node):
    if node is None:
        return
    print_inorder(node.left)
    print(node.val, end=' ')
    print_inorder(node.right)


arr = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
n = len(arr)

root = insert_level_order(arr, None, 0, n)

solution = Solution()
gst_root = solution.bstToGst(root)
print_inorder(gst_root)
