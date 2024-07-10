class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        balance = (numBottles - 1) // (numExchange - 1)
        drinkin = numBottles + balance

        return drinkin


numBottles = 9
numExchange = 3
sol = Solution()
print(sol.numWaterBottles(numBottles, numExchange))
