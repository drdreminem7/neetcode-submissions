class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max, n = -1, len(arr)
        for i in range(n - 1, -1, -1):
            temp = curr_max
            curr_max = max(arr[i], curr_max)
            arr[i] = temp

        return arr