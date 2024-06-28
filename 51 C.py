class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        operations = 0

        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i + 1] = 1 - nums[i + 1]
                nums[i + 2] = 1 - nums[i + 2]
                operations += 1

        if nums[-2] == 0 or nums[-1] == 0:
            return -1

        return operations



nums = [0,1,1,1,0,0]
sol = Solution()
print(sol.minOperations(nums))
