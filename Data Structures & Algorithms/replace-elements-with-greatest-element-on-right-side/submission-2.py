class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n, max_num = len(arr), -1
        for i in range(n - 1, -1, -1):
            curr_max = max_num
            max_num = max(max_num, arr[i])
            arr[i] = curr_max

        return arr