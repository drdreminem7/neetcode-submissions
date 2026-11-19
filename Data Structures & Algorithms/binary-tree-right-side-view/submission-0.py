# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue = [root]
        result = []

        while len(queue) > 0:
            levelSize = len(queue)
            while levelSize > 0:
                front = queue[0]
                queue.pop(0)

                if front.left: queue.append(front.left)
                if front.right: queue.append(front.right)

                if levelSize == 1: result.append(front.val)
                levelSize -= 1

        return result