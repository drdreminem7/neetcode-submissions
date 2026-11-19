# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min_value, max_value = float("-inf"), float("inf")

        def isValid(root, min_value, max_value):
            if not root: return True
            return min_value < root.val < max_value and isValid(root.left, min_value, root.val) and isValid(root.right, root.val, max_value) 

        return isValid(root, min_value, max_value)

            