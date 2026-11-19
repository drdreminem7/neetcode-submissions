class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        occurrences = [0] * 26
        for i in range(len(s)):
            occurrences[ord(s[i]) - ord('a')] += 1
            occurrences[ord(t[i]) - ord('a')] -= 1
            
        for ch in occurrences: 
            if ch != 0: return False
        return True