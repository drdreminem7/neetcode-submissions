class Solution:
    def decodeString(self, s: str) -> str:
        stringStack = [""]
        multiplierStack = []
        num = 0

        for ch in s:
            if ch.isalpha(): stringStack[-1] += ch
            elif ch.isdigit(): num = num * 10 + int(ch)
            elif ch == "[":
                stringStack.append("")
                multiplierStack.append(num)
                num = 0
            else:
                result = stringStack.pop() * int(multiplierStack.pop())
                stringStack[-1] += result

        return stringStack[-1]