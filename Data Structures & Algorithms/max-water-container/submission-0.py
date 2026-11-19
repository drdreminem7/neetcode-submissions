class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1
        maxWater = 0
        while start < end:
            curr = min(heights[start], heights[end]) * (end - start)
            if maxWater < curr: maxWater = curr

            if heights[start] <= heights[end]: start += 1
            else: end -= 1
        return maxWater