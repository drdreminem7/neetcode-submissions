class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def check(s, t):
            hash_map = {}
            for i in range(len(s)):
                if s[i] in hash_map and hash_map[s[i]] != t[i]:
                    return False
                hash_map[s[i]] = t[i]
            return True
        
        return check(s, t) and check(t, s)