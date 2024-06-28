


class Solution(object):
    def maxTotalReward(self, rewardValues):
        n = len(rewardValues)


        max_with_curr = 0
        max_without_curr = 0


        for i in range(n):
           
            new_max_with_curr = max_without_curr + rewardValues[i]


            max_without_curr = max(max_with_curr, max_without_curr)

            max_with_curr = new_max_with_curr

        return max(max_with_curr, max_without_curr)
rewardValues = [1, 6, 4, 3, 2]
rewardValues1 = [1, 1,3,3]

sol = Solution()
print(sol.maxTotalReward(rewardValues1))
