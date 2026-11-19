class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)
        n = len(nums) // 2

        print(count)
        for value in count.values():
            if value % 2:
                return False
            n -= (value / 2)

        return n == 0