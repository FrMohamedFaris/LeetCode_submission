class Solution(object):
    def numberOfPermutations(self, n, requirements):

        MOD = 10 ** 9 + 7

        dp = [[0] * (n * (n - 1) // 2 + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for endi, cnti in requirements:
            new_dp = [[0] * (n * (n - 1) // 2 + 1) for _ in range(n + 1)]

            for k in range(n + 1):
                for x in range(n * (n - 1) // 2 + 1):
                    if dp[k][x] > 0:
                        new_dp[k][x] = (new_dp[k][x] + dp[k][x]) % MOD
                        if k + 1 <= n:
                            new_dp[k + 1][x + k] = (new_dp[k + 1][x + k] + dp[k][x]) % MOD

            dp = new_dp

        result = 0
        for cnti in range(n * (n - 1) // 2 + 1):
            result = (result + dp[n][cnti]) % MOD

        return result


n = 3
requirements = [[2, 2], [1, 1], [0, 0]]
sol = Solution()
print(sol.numberOfPermutations(n, requirements))
