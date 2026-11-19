class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        n = len(pattern)

        if n != len(words): 
            return False

        hash_map = {}

        for i in range(n):
            if (pattern[i] in hash_map and hash_map[pattern[i]] != words[i]) or (words[i] in hash_map and hash_map[words[i]] != pattern[i]):
                return False
            hash_map[pattern[i]] = words[i]
            hash_map[words[i]] = pattern[i]
        
        return True