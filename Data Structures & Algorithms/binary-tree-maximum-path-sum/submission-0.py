# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_so_far = float("-inf")
        def dfs(root):
            nonlocal max_so_far
            if not root: return 0

            left_max = dfs(root.left)
            right_max = dfs(root.right)

            left_val = max(left_max, 0)
            right_val = max(right_max, 0)

            max_so_far = max(max_so_far, left_val + root.val + right_val)

            return max(left_val + root.val, right_val + root.val)

        dfs(root)
        return max_so_far
