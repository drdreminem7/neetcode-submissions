# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(root, key: int):
            if not root: return None
            if root.val > key: root.left = delete(root.left, key)
            elif root.val < key: root.right = delete(root.right, key)
            else:
                if not root.left and not root.right: return None
                if not root.left: return root.right
                if not root.right: return root.left

                iter = root.right
                while iter.left:
                    iter = iter.left

                root.val = iter.val
                root.right = delete(root.right, root.val)
            
            return root
            
        root = delete(root, key)
        return root