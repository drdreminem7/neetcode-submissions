class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        summ = sum(nums)
        if summ % k != 0: return False

        length = summ // k
        sol = [0] * k
        n = len(nums)

        nums.sort(reverse=True)
        if nums[0] > length: return False

        def backtrack(i):
            if i == n:
                return True

            seen = set()

            for j in range(k):
                if sol[j] in seen: continue

                if sol[j] + nums[i] <= length:
                    seen.add(sol[j])
                    sol[j] += nums[i]
                    if backtrack(i + 1):
                        return True
                    sol[j] -= nums[i]
            
            return False

        return backtrack(0)