class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash_map = {}
        count = 0
        for i in range(len(nums)):
            if nums[i] in hash_map:
                count += hash_map[nums[i]]
                hash_map[nums[i]] += 1
            else:
                hash_map[nums[i]] = 1

        return count