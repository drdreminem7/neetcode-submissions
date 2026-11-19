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

    def merge(self, nums: List[int], leftArray: List[int], rightArray: List[int]) -> None:
        i, j = 0, 0

        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] <= rightArray[j]:
                nums[i + j] = leftArray[i]
                i += 1
            else:
                nums[i + j] = rightArray[j]
                j += 1

        while i < len(leftArray):
            nums[i + j] = leftArray[i]
            i += 1

        while j < len(rightArray):
            nums[i + j] = rightArray[j]
            j += 1

    def mergeSort(self, nums:List[int]) -> None:
        length = len(nums)
        if length <= 1: return

        middle = length // 2
        leftArray = nums[:middle]
        rightArray = nums[middle:]

        j = 0
        for i in range(length):
            if i < middle: leftArray[i] = nums[i]
            else:
                rightArray[j] = nums[i]
                j += 1

        self.mergeSort(leftArray)
        self.mergeSort(rightArray)
        self.merge(nums, leftArray, rightArray)

    def sortArray(self, nums: List[int]) -> List[int]:
        # self.quickSelect(nums, 0, len(nums) - 1)
        self.mergeSort(nums)
        return nums