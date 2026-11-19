from random import randrange

class Solution:
    def partition(self, nums: List[int], start: int, end: int) -> int:
        initialPivotIndex = randrange(start, end + 1)
        nums[end], nums[initialPivotIndex] = nums[initialPivotIndex], nums[end]

        pivot = nums[end]
        i = start - 1

        for j in range(start, end):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        i += 1
        nums[i], nums[end] = nums[end], nums[i]

        return i

    def quickSelect(self, nums:List[int], start: int, end: start) -> None:
        if start >= end: return
        pivotIndex = self.partition(nums, start, end)

        self.quickSelect(nums, start, pivotIndex - 1)
        self.quickSelect(nums, pivotIndex + 1, end)
        

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSelect(nums, 0, len(nums) - 1)
        return nums