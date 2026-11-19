class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        n = len(s)
        hash_map = [0] * 26
        for i in range(n):
            hash_map[ord(s[i]) - ord("a")] += 1
            hash_map[ord(t[i]) - ord("a")] -= 1
        
        for i in range(26):
            if hash_map[i] != 0:
                return False
        
        return True