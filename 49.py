class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        prefix_count = {0: 1}
        count = 0
        result = 0

        for i in nums:
            if i % 2 != 0:
                count += 1

            if count - k in prefix_count:
                result += prefix_count[count - k]

            if count in prefix_count:
                prefix_count[count] += 1
            else:
                prefix_count[count] = 1

        return result


nums = [1, 1, 2, 1, 1]
k = 3
sol = Solution()
print(sol.numberOfSubarrays(nums, k))
