class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = 0
        current_time = 0
        for arrival, cooking_time in customers:
            if current_time < arrival:
                current_time = arrival

            current_time += cooking_time
            total += (current_time - arrival)

        return total / len(customers)