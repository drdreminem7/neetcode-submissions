# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = [root]
        result = []

        while len(queue) > 0:
            levelSize = len(queue)
            result.append([])
            while levelSize > 0:
                front = queue[0]
                queue.pop(0)

                if front.left: queue.append(front.left)
                if front.right: queue.append(front.right)

                result[-1].append(front.val)
                levelSize -= 1

        return result