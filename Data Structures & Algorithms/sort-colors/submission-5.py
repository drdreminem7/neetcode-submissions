class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0] * 3
        for num in nums:
            counter[num] += 1
        
        print(counter)

        index = 0
        for i in range(3):
            nums[index:index + counter[i]] = [i] * counter[i]
            index += counter[i]
