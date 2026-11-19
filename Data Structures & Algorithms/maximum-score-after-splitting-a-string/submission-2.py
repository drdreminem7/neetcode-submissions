class Solution:
    def maxScore(self, s: str) -> int:
        curr_max, zeros = 0, 0
        n = len(s)
        for digit in s:
            if digit == "0":
                zeros += 1
        
        left_side_zeros = 0
        for i in range(n - 1):
            if s[i] == "0":
                left_side_zeros += 1

            right_side_ones = n - (i + 1) - (zeros - left_side_zeros)

            curr_max = max(curr_max, left_side_zeros + right_side_ones)

        return curr_max