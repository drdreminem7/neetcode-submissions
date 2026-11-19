class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        contender = -1
        for key, value in count.items():
            if key == value:
                contender = max(contender, key)

        return contender