from collections import defaultdict
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        seenLetters = defaultdict(int)
        for word in strs:
            for i in range(len(word)):
                seenLetters[(word[i], i)] += 1

        res = ""
        for i in range(len(strs[0])):
            if seenLetters[(strs[0][i], i)] != len(strs): break
            res += strs[0][i]

        return res

        

        