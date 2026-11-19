class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ones_indexes = []
        for i in range(n):
            if boxes[i] == "1":
                ones_indexes.append(i)

        res = [0] * n
        for i in range(n):
            for one_index in ones_indexes:
                if i == one_index:
                    continue
                res[i] += abs(i - one_index)

        return res
            
