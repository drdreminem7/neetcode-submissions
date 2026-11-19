class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexedNums = {}
        for i in range(len(nums)):
            if target - nums[i] in indexedNums:
                return [indexedNums[target - nums[i]], i]
            indexedNums[nums[i]] = i

        return [-1,-1]