class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        msIndex = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while msIndex and temperatures[i] > temperatures[msIndex[-1]]:
                result[msIndex[-1]] = i - msIndex[-1]
                msIndex.pop()
            msIndex.append(i)

        return result