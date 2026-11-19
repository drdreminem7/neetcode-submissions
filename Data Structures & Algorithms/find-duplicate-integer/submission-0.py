class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            abs_val = abs(nums[i])
            if nums[abs_val - 1] < 0: return abs_val
            nums[abs_val - 1] *= -1
        return -1