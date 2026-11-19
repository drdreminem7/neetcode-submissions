class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occurrences = [0] * 26
        if len(s) != len(t): return False
        for i in range(len(s)):
            occurrences[ord(s[i]) - ord('a')] += 1
            occurrences[ord(t[i]) - ord('a')] -= 1
        for ch in occurrences: 
            if ch != 0: return False
        return True