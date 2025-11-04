class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]  # one way to make 0

        for c in candidates:
            for t in range(c, target + 1):
                for comb in dp[t - c]:
                    newComb = comb.copy()
                    newComb.append(c)
                    dp[t].append(newComb)
        return dp[target]