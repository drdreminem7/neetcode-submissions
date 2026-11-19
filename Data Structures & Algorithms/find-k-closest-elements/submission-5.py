class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start, end = 0, len(arr) - 1
        while end - start >= k:
            if abs(x - arr[start]) <= abs(x - arr[end]):
                end -= 1
            else:
                start += 1
            
        return arr[start: start + k]
            