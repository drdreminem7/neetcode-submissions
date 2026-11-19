class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for word in strs:
            seen_letters = [0] * 26
            for ch in word:
                seen_letters[ord(ch) - ord("a")] += 1
            hash_map[tuple(seen_letters)].append(word)
        return list(hash_map.values())
