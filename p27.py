class Solution(object):
    def checkSubarraySum(self, nums, k):
        prefix_mod = {0: -1}
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            mod = prefix_sum % k

            if mod in prefix_mod:
                if i - prefix_mod[mod] > 1:
                    return True
            else:
                prefix_mod[mod] = i

        return False


nums = [23, 2, 4, 6, 7]
k = 6
sol = Solution()
print(sol.checkSubarraySum(nums, k))
