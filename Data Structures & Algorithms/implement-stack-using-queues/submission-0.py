class MyStack:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)
        while self.output:
            self.input.append(self.output.pop(0))

        self.input, self.output = self.output, self.input

    def pop(self) -> int:
        return self.output.pop(0)

    def top(self) -> int:
        return self.output[0]

    def empty(self) -> bool:
        return len(self.output) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()