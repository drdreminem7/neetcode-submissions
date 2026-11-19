class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        max_odd, min_even = 0, float("inf")
        for freq in counter.values():
            if freq & 1:
                max_odd = max(max_odd, freq)
            else:
                min_even = min(min_even, freq)

        return max_odd - min_even