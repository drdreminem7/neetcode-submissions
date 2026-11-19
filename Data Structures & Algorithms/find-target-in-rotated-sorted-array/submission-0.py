class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start, end = 0, n - 1
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[end]: start = mid + 1
            else: end = mid

        min_index = end

        if min_index == 0:
            start, end = 0, n - 1
        elif target >= nums[0] and target <= nums[min_index - 1]:
            start, end = 0, min_index - 1
        else:
            start, end = min_index, n - 1

        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target: return mid
            elif nums[mid] > target: end = mid - 1
            else: start = mid + 1

        return -1





