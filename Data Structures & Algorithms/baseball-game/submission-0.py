class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
                total += stack[-1]
            elif op == "D":
                stack.append(stack[-1] * 2)
                total += stack[-1]
            elif op == "C":
                total -= stack.pop()
            else:
                stack.append(int(op))
                total += stack[-1]

        return total