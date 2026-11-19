class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexedNums = defaultdict(int)
        for i in range(len(nums)):
            if target - nums[i] in indexedNums and i != indexedNums[nums[i]]:
                return [indexedNums[target - nums[i]], i]
            indexedNums[nums[i]] = i
        return [-1, -1]
