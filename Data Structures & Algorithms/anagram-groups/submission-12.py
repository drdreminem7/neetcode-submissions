class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for word in strs:
            letter_counter = [0] * 26
            for ch in word:
                letter_counter[ord(ch) - ord("a")] += 1
            hash_map[tuple(letter_counter)].append(word)
        return list(hash_map.values())