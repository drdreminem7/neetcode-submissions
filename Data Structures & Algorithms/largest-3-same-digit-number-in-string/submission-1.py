class Solution:
    def largestGoodInteger(self, num: str) -> str:
        contender = ""
        for i in range(2, len(num)):
            if num[i - 2] == num[i - 1] == num[i]:
                if not contender or int(contender) < int(num[i-2:i+1]):
                    contender = num[i - 2: i + 1]

        return contender