class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        seenNums = defaultdict(int)
        for i in range(len(nums)):
            seenNums[nums[i]] += 1

        nums.clear()
        for i in range(3):
            nums.extend([i] * seenNums[i])

        return nums
        