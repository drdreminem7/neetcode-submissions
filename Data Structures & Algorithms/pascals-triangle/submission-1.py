class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows - 1):
            temp = [0] + res[i] + [0]
            new_row = []
            for i in range(1, len(temp)):
                new_row.append(temp[i - 1] + temp[i])
            res.append(new_row)
        return res