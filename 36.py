class Solution(object):
    def minPatches(self, nums, n):
        patches = 0
        miss = 1
        i = 0

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patches += 1

        return patches


sol = Solution()
nums = [1, 3]
n = 6
print(sol.minPatches(nums, n))
