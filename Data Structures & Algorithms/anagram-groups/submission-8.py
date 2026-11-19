class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            seenLetters = [0] * 26
            for letter in word:
                seenLetters[ord(letter) - ord('a')] += 1

            res[tuple(seenLetters)].append(word)

        return list(res.values())