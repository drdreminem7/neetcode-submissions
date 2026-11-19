class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            for ch in strs[i]:
                if j == len(prefix) or ch != prefix[j]:
                    break
                j += 1
            
            prefix = prefix[:j]
        return prefix