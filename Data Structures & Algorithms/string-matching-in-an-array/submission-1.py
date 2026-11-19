class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for word in words:
            for prefix in words:
                if prefix in word and prefix is not word and prefix not in result:
                    result.append(prefix)

        return result