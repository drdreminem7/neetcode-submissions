class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        contender, count = nums[0], 1
        for num in nums:
            if contender != num:
                count -= 1
                if count < 0: 
                    contender = num
                    count = 1
            else: count += 1

        return contender