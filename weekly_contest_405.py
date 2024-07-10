class Solution(object):
    def countSubarrays(self, nums, k):
        count = 0
        n = len(nums)
        prefix_count = {}
        current_and = 0

        for i in range(n):
            current_and &= nums[i]

            if current_and == k:
                count += 1

            if current_and in prefix_count:
                prefix_count[current_and] += 1
            else:
                prefix_count[current_and] = 1

            target_and = current_and & k
            if target_and in prefix_count:
                count += prefix_count[target_and]

        return count


nums = [1, 1, 1]
k = 1
sol = Solution()
print(sol.countSubarrays(nums, k))
