class Solution(object):
    def minIncrementForUnique(self, nums):
        nums.sort()
        moves = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                increment = nums[i - 1] + 1 - nums[i]
                moves += increment
                nums[i] = nums[i - 1] + 1
        return moves


nums = [1, 2, 2]
sol = Solution()
print(sol.minIncrementForUnique(nums))
