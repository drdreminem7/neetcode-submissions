class Solution:
    def isValid(self, s: str) -> bool:
        opposite = {")": "(", "]": "[", "}": "{"}
        stack = []

        for ch in s:
            if ch in opposite:
                if not stack or stack[-1] != opposite[ch]: return False
                stack.pop()
            else: stack.append(ch)
        
        return True if not stack else False