from collections import defaultdict
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs:
            j = 0
            while j < min(len(prefix), len(word)):
                if word[j] != prefix[j]:
                    break
                j += 1

            prefix = prefix[:j]

        return prefix

        