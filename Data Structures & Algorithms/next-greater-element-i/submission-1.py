class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = {num : i for i, num in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                top = stack.pop()
                res[hash_map[top]] = nums2[i]

            if nums2[i] in hash_map:
                stack.append(nums2[i])

        return res