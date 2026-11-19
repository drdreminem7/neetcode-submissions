class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, numZeros, zeroIndex = 1, 0, -1
        for i,num in enumerate(nums):
            if num == 0:
                numZeros += 1
                zeroIndex = i
            else: prod *= num

        if numZeros >= 2: return [0] * len(nums)
        
        if zeroIndex != -1: return [0 if num != 0 else prod for num in nums]

        return [prod // num for num in nums]

