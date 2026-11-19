class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        contender, count = nums[0], 1
        for i in range(1, len(nums)):
            if contender != nums[i]:
                count -= 1
                if count < 0:
                    contender, count = nums[i], 1
            else:
                count += 1

        return contender