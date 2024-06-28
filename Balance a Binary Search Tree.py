class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder_traversal(self, root):
        """Perform in-order traversal of the BST and return a sorted array of node values."""
        if not root:
            return []
        return self.inorder_traversal(root.left) + [root.val] + self.inorder_traversal(root.right)

    def sorted_array_to_bst(self, nums):
        """Convert sorted array to a balanced BST."""
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sorted_array_to_bst(nums[:mid])
        root.right = self.sorted_array_to_bst(nums[mid + 1:])
        return root

    def balanceBST(self, root):
        """Balance the given BST."""
        sorted_values = self.inorder_traversal(root)
        return self.sorted_array_to_bst(sorted_values)


from collections import deque


def print_tree(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            if node:
                current_level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                current_level.append(None)
        result.append(current_level)

    while result[-1] == [None] * len(result[-1]):
        result.pop()
    return result


root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)

solution = Solution()
balanced_root = solution.balanceBST(root)
print(print_tree(balanced_root))
