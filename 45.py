from collections import deque


class Solution(object):
    def maximumRobots(self, chargeTimes, runningCosts, budget):
        """
        :type chargeTimes: List[int]
        :type runningCosts: List[int]
        :type budget: int
        :rtype: int
        """

        chargeTimes.sort()

        left = 0


        max_robots = 0
        total_running_cost = 0
        max_charge_deque = deque()

        for right in range(len(chargeTimes)):
            total_running_cost += runningCosts[right]


            while max_charge_deque and chargeTimes[max_charge_deque[-1]] <= chargeTimes[right]:
                max_charge_deque.pop()
            max_charge_deque.append(right)


            while max_charge_deque and (
                    chargeTimes[max_charge_deque[0]] + (right - left + 1) * total_running_cost) > budget:
                if max_charge_deque[0] == left:
                    max_charge_deque.popleft()
                total_running_cost -= runningCosts[left]
                left += 1


            max_robots = max(max_robots, right - left + 1)

        return max_robots


chargeTimes = [3, 6, 1, 3, 4]
runningCosts = [2, 1, 3, 4, 5]
budget = 25
sol = Solution()
print(sol.maximumRobots(chargeTimes, runningCosts, budget))
