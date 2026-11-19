class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: 
            return True
        if len(s) > len(t):
            return False

        index = 0
        for ch in t:
            if ch == s[index]:
                index += 1
                if index == len(s):
                    return True
            
        return False

