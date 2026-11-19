class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        start, end = 1, length - 2
        while start <= end:
            m = start + (end - start) // 2
            left, mid, right = mountainArr.get(m - 1), mountainArr.get(m), mountainArr.get(m + 1)
            if left < mid < right:
                start = m + 1
            elif left > mid > right:
                end = m - 1
            else: 
                break

        peak = m
        start, end = 0, peak
        while start <= end:
            m = start + (end - start) // 2
            mid = mountainArr.get(m)

            if mid == target: return m
            elif mid > target: end = m - 1
            else: start = m + 1

        start, end = peak, length - 1
        while start <= end:
            m = start + (end - start) // 2
            mid = mountainArr.get(m)

            if mid == target: return m
            elif mid < target: end = m - 1
            else: start = m + 1

        return -1