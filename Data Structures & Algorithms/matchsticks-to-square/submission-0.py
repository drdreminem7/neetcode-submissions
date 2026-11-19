class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        square = sum(matchsticks)
        if square % 4 != 0: return False
        matchsticks.sort(reverse=True)

        side_length = square / 4
        n = len(matchsticks)
        sides = [0] * 4
        

        def backtrack(i):
            if i == n:
                return True

            for j in range(4):
                if sides[j] + matchsticks[i] <= side_length:
                    sides[j] += matchsticks[i]
                    if backtrack(i + 1):
                        return True
                    sides[j] -= matchsticks[i]

            return False

        return backtrack(0)