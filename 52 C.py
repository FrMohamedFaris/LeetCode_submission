class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        flips = 0
        flipped = False

        for i in range(n):
            current_state = nums[i] if not flipped else 1 - nums[i]
            if current_state == 0:
                flips += 1
                flipped = not flipped

        return flips


nums = [0, 1, 1, 0, 1]
sol = Solution()
print(sol.minOperations(nums))
