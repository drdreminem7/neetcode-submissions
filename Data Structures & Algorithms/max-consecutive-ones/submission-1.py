class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_count = 1 if nums[0] else 0
        max_count = curr_count 
        for i in range(1, len(nums)):
            if nums[i] == 1:
                curr_count += 1
            else:
                max_count = max(max_count, curr_count)
                curr_count = 0
        
        return max(max_count, curr_count)