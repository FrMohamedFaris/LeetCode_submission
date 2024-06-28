class Solution(object):
    def minimumOperations(self, nums):

        operation = 0
        for i in nums:
            remainder = i % 3
            if remainder == 1:
                operation += 1
            elif remainder == 2:
                operation += 1
        return operation


nums = [1, 2, 3, 4]
sol = Solution()
print(sol.minimumOperations(nums))
