class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        n = len(nums)
        for num in nums:
            seen.add(num)

        solution = []
        for i in range(1, n + 1):
            if i not in seen:
                solution.append(i)

        return solution