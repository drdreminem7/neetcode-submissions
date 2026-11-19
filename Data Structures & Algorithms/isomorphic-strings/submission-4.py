class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_map = {}
        hash_set = set()
        for i in range(len(s)):
            if (t[i] in hash_map and hash_map[t[i]] != s[i]) or (t[i] not in hash_map and s[i] in hash_set):
                return False
            hash_map[t[i]] = s[i]
            hash_set.add(s[i])

        return True