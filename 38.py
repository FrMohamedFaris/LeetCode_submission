class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        max_profit = 0
        total_profit = 0
        worker.sort()
        jobs = sorted(zip(difficulty, profit))
        n = len(jobs)
        i = 0

        for ability in worker:
            while i < n and jobs[i][0] <= ability:
                max_profit = max(max_profit, jobs[i][1])
                i += 1
            total_profit += max_profit

        return total_profit


# difficulty = [2, 4, 6, 8, 10]
# profit = [10, 20, 30, 40, 50]
# worker = [4, 5, 6, 7]
difficulty = [13, 37, 58]
profit = [4, 90, 96]
worker = [34, 73, 45]
sol = Solution()
print(sol.maxProfitAssignment(difficulty, profit, worker))
