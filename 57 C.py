class Solution(object):
    def maximumTotalCost(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        max_cost = 0
        current_sum = 0

        for i in range(n):
            if i % 2 == 0:
                current_sum += nums[i]
            else:
                current_sum -= nums[i]

            if current_sum > max_cost:
                max_cost = current_sum

        return max_cost


nums = [1, -2, 3, 4]
sol = Solution()
print(sol.maximumTotalCost(nums))
