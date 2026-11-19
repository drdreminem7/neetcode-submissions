class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            occurrences = [0] * 26
            for letter in s:
                occurrences[ord(letter) - ord('a')] += 1

            res[tuple(occurrences)].append(s)
        return list(res.values())