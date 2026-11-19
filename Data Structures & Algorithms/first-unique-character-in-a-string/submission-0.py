class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}
        n = len(s)
        
        for i in range(n):
            hash_map[s[i]] = i

        for i in range(n):
            if i == hash_map[s[i]]:
                return i
            else:
                hash_map[s[i]] = -1

        return -1