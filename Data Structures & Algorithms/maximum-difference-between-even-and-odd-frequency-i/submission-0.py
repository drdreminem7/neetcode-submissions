class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        odd_max, even_min = 0, len(s)
        for freq in count.values():
            if freq & 1:
                odd_max = max(odd_max, freq)
            else:
                even_min = min(even_min, freq)
        return odd_max - even_min