class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(n):
            if n - i <= nums[i]:
                if i == 0 or n - i > nums[i - 1]:
                    return n - i

        return -1