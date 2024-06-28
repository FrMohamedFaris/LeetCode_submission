class Solution(object):
    def threeSum(self, nums):
        nums.sort()

        val = []

        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, n):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue

                    sum = nums[i] + nums[j] + nums[k]
                    if sum == 0:
                        val.append((nums[i], nums[j], nums[k]))
        return val


nums = [-1, 0, 1, 2, -1, -4]
sol = Solution()
print(sol.threeSum(nums))
