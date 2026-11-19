class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        nums = [0, 1, 0]

        for i in range(rowIndex):
            for j in range(len(nums) - 1):
                nums[j] = nums[j] + nums[j + 1]
            nums = [0] + nums
            print(nums)

        return nums[1:len(nums) - 1]