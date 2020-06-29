            # week five day one

class SolutionOne:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        
        for _ in range(1, m):
            for i in range(1, n):
                dp[i] += dp[i - 1]
        
        return dp[-1]
        