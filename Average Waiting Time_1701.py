class Solution:
    def averageWaitingTime(self, customers):
        idle = 0
        wait = 0
        for i in customers:
            idle = max(i[0], idle) + i[1]

            wait += idle - i[0]

        return wait / len(customers)


customers = [[5, 2], [5, 4], [10, 3], [20, 1]]
sol = Solution()
print(sol.averageWaitingTime(customers))
