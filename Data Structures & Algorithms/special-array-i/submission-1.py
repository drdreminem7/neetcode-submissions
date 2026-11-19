class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        
        for i in range(1, n):
            if not ((nums[i] - nums[i - 1]) & 1):
                return False
                
        return True