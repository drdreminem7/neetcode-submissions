class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        duplicate = 0
        for i in range(n):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                duplicate = abs(nums[i])
            else:
                nums[index] *= -1

        for i in range(n):
            if nums[i] > 0:
                return [duplicate, i + 1]

        return [-1, -1]
        
