class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        n = len(customers)

        satisfaction_count = 0
        max_add_satisfaction = 0
        current_add_satisfaction = 0

        for i in range(n):
            if grumpy[i] == 0:
                satisfaction_count += customers[i]
            else:
                if i < minutes:
                    current_add_satisfaction += customers[i]


        max_add_satisfaction = current_add_satisfaction
        

        for i in range(minutes,n):
            if grumpy[i] == 1:
                current_add_satisfaction += customers[i]
            elif grumpy[i - minutes] == 1:
                current_add_satisfaction -= customers[i - minutes]
            max_add_satisfaction = max(max_add_satisfaction, current_add_satisfaction)

        return satisfaction_count + max_add_satisfaction


customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
minutes = 3
sol = Solution()
print(sol.maxSatisfied(customers, grumpy, minutes))
