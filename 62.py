class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.reverse()

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] -1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


nums = [3, 4, -1, 1]
sol = Solution()
print(sol.firstMissingPositive(nums))
