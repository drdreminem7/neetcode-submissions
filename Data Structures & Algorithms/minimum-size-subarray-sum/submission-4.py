class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        smallest = float("inf")
        start = 0
        total = 0

        for end in range(n):
            total += nums[end]
            while total >= target:
                smallest = min(smallest, end - start + 1)
                total -= nums[start]
                start += 1

        return smallest if smallest != float("inf") else 0