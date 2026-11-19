class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zero_index, prod = -1, 1
        for i in range(n):
            if nums[i] == 0:
                if zero_index != -1:
                    return [0] * n
                zero_index = i
            else:
                prod *= nums[i]

        if zero_index != -1:
            return [0] * zero_index + [prod] + [0] * (n - zero_index - 1)

        for i in range(n):
            nums[i] = prod // nums[i]

        return nums