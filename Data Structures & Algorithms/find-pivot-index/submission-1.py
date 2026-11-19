class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n, curr_sum = len(nums), 0
        prefix_sum = [0] * (n + 2)
        for i in range(n):
            curr_sum += nums[i]
            prefix_sum[i + 1] = curr_sum
        prefix_sum[-1] = prefix_sum[-2]

        for i in range(1, n + 1):
            if prefix_sum[-1] - prefix_sum[i - 1] == prefix_sum[i]:
                return i - 1
        
        return -1

        
