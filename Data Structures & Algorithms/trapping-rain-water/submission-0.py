class Solution:
    def trap(self, height: List[int]) -> int:
        stack_right = []
        for num in reversed(height):
            if not stack_right or stack_right[-1] <= num:
                stack_right.append(num)

        highest_left = -1
        sum = 0

        for h in height:
            if h >= highest_left: highest_left = h

            sum += max(min(highest_left, stack_right[-1]) - h, 0)
            if stack_right and h == stack_right[-1]:
                stack_right.pop()
        return sum