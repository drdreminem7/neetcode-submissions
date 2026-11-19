# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_hm = {val:index for index, val in enumerate(inorder)}
        preorder_index = 0

        def arr_to_tree(start, end):
            nonlocal preorder_index
            if start > end: return None

            root_val = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(root_val)

            root.left = arr_to_tree(start, inorder_hm[root_val] - 1)
            root.right = arr_to_tree(inorder_hm[root_val] + 1, end)

            return root

        return arr_to_tree(0, len(preorder) - 1)
