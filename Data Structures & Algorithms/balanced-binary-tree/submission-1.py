# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def height(root):
            nonlocal balanced
            if not root: return 0

            left_d = height(root.left)
            right_d = height(root.right)

            if abs(left_d - right_d) > 1:
                balanced = False
                return 0

            return 1 + max(left_d, right_d)

        height(root)

        return balanced