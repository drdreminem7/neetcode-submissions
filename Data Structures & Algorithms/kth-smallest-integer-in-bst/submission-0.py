# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        def inorder_traversal(root):
            if not root: return
            inorder_traversal(root.left)
            nodes.append(root.val)
            inorder_traversal(root.right)
        inorder_traversal(root)
        return nodes[k - 1]