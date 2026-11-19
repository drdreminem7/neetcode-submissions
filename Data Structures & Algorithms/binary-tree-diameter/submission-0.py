# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest_diameter = 0

        def height(root: Optional[TreeNode]):
            nonlocal largest_diameter
            if not root: return 0

            left_d = height(root.left)
            right_d = height(root.right)
            diameter = left_d + right_d

            largest_diameter = max(largest_diameter, diameter)

            return 1 + max(left_d, right_d)
        
        height(root)
        return largest_diameter


