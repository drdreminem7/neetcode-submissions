class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_decreasing_count = 1
        curr_count = 1
        last_num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < last_num:
                curr_count += 1
                max_decreasing_count = max(max_decreasing_count, curr_count)
                last_num = nums[i]
            else:
                last_num = nums[i]
                curr_count = 1

        max_increasing_count = 1
        curr_count = 1
        last_num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > last_num:
                curr_count += 1
                max_increasing_count = max(max_increasing_count, curr_count)
                last_num = nums[i]
            else:
                last_num = nums[i]
                curr_count = 1

        return max(max_decreasing_count, max_increasing_count)

        