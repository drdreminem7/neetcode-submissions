class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        pair = (nums[0], nums[1]) if nums[0] < nums[1] else (nums[1], nums[0])
        for i in range(2, len(nums)):
            if nums[i] > pair[0]:
                if nums[i] > pair[1]:
                    pair = (pair[1], nums[i])
                else:
                    pair = (nums[i], pair[1])

        max_prod = pair[0] * pair[1]

        pair = (nums[0], nums[1]) if nums[0] < nums[1] else (nums[1], nums[0])
        for i in range(2, len(nums)):
            if nums[i] < pair[1]:
                if nums[i] < pair[0]:
                    pair = (nums[i], pair[0])
                else:
                    pair = (pair[0], nums[i])

        min_prod = pair[0] * pair[1]
        print(pair)

        return max_prod - min_prod
