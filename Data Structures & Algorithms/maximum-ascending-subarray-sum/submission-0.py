class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr, max_sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += nums[i]
                max_sum = max(curr, max_sum)
            else:
                curr = nums[i]
        return max_sum