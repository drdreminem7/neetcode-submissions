class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1Copy = nums1.copy()
        i = j = 0

        while i < m and j < n:
            if nums1Copy[i] <= nums2[j]:
                nums1[i + j] = nums1Copy[i]
                i += 1
            else:
                nums1[i + j] = nums2[j]
                j += 1

        while i < m: 
            nums1[i + j] = nums1Copy[i]
            i += 1

        while j < n: 
            nums1[i + j] = nums2[j]
            j += 1
        