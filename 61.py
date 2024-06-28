from collections import deque


class Solution(object):
    def minimumTime(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dq = deque()
        current_cost = 0
        min_cost = float('inf')

        for i in range(n):
            if s[i] == '1':
                current_cost += 2
            else:
                current_cost = max(0, current_cost - 1)

            min_cost = min(min_cost, current_cost)

        left_cost = 0
        for i in range(n):
            if s[i] == '1':
                left_cost += 1
            else:
                left_cost = max(0, left_cost - 1)
            min_cost = min(min_cost, left_cost + (n - i - 1))

        return min_cost


s = "1100101"
sol = Solution()
print(sol.minimumTime(s))
