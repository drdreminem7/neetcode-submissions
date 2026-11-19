class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        indexOfZero = -1

        for i in range(len(nums)):
            if nums[i] == 0 and indexOfZero >= 0: return [0] * len(nums)
            if nums[i] == 0: 
                indexOfZero = i
                continue

            prod *= nums[i]

        if indexOfZero >= 0:
            nums = [0] * len(nums)
            nums[indexOfZero] = prod
            return nums

        for i in range(len(nums)):
            nums[i] = prod // nums[i]

        return nums